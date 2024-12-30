import numpy as np

class MetropolisHastings():
    def __init__(self, target_pdf, step_method, proposal_pdf, temperature=None):
        self.target_pdf = target_pdf
        self.step_method = step_method
        self.proposal_pdf = proposal_pdf
        self.samples = np.array([])
        if temperature:
            self.temperature = temperature
    
    def propose(self, x):
        return self.step_method(x)

    def accept(self, x, x_next):
        p_xnext = self.target_pdf(x_next)
        p_x = self.target_pdf(x)
        q_xnext_x = self.proposal_pdf(x_next, x)
        q_x_xnext = self.proposal_pdf(x, x_next)
        if (p_x * q_x_xnext) == 0:
            return False          
        A = (p_xnext * q_xnext_x) / (p_x * q_x_xnext)
        return np.random.uniform(0, 1) < np.min([1, A])

    def burn_in(self, burn_in_steps, initial_value):
        """
        Perform the burn-in phase to stabilize the chain.
        """
        x = initial_value
        for _ in range(burn_in_steps):
            x_next = self.propose(x)
            if self.accept(x, x_next):
                x = x_next
        self._burned_in = True
        self._x = x

    def run(self, n_samples, start_value=[-1,1], burn_in_steps=10000, max_steps=None):
        """
        Run the MCMC sampling.
        """
        # Burn-in phase, if not yet
        if not hasattr(self, '_burned_in'):
            l, r = start_value
            self.burn_in(burn_in_steps, np.random.uniform(l, r))
        
        # calculate max_steps if not provided
        if not max_steps:
            max_steps = 10 * n_samples + burn_in_steps
        else:
            max_steps = max_steps + burn_in_steps
            
        # Sampling phase
        samples, steps = np.array([]), 0
        while len(samples) < n_samples:
            x_next = self.propose(self._x)
            accept = self.accept(self._x, x_next)
            if accept:
                self._x = x_next
                samples = np.append(samples, self._x)
            
            # check if max_iter is reached, if so exit from iteration
            steps += 1
            if steps > max_steps:
                print("Processed stop because maximum steps is reached")
                break             
        
        # Store the sampling result as class attributes
        self.samples = np.concatenate([self.samples, samples])
        # return samples
        return samples


class TemperredMetropolisHastings(MetropolisHastings):
    def __init__(self, target_pdf, step_method, proposal_pdf, temperatures):
        super().__init__(target_pdf, step_method, proposal_pdf)
        self.init_tempered_samplers(temperatures)
        
    def init_tempered_samplers(self, temperatures):
        self.temperatures = temperatures
        self.chains = []
        for T in self.temperatures:
            chain = MetropolisHastings(
                target_pdf = lambda x, T=T: self.target_pdf(x, T),
                step_method = self.step_method,
                proposal_pdf = self.proposal_pdf,
                temperature = T
            )
            self.chains.append(chain)

    def swap_chains(self):
        def _swap(cold, hot):
            x_cold, x_hot = cold._x, hot._x
            pcold_x_cold = cold.target_pdf(x_cold)
            pcold_x_hot = cold.target_pdf(x_hot)
            phot_x_hot = hot.target_pdf(x_hot)
            phot_x_cold = hot.target_pdf(x_cold)
            acceptance_ratio = (pcold_x_hot * phot_x_cold) / (pcold_x_cold * phot_x_hot)
            return np.random.uniform(0, 1) < np.min([1, acceptance_ratio])
        
        # perform swap across chains
        chain_states = [c._x for c in self.chains]
        n_chains = len(chain_states)
        for i in range(n_chains - 1):
            cold, hot = self.chains[i], self.chains[i+1]
            if _swap(cold, hot):
                chain_states[i], chain_states[i+1] = hot._x, cold._x
                
        for i in range(n_chains):
            self.chains[i]._x = chain_states[i]
        
    def run(self, n_samples, start_value=[-1,1], burn_in_steps=5000, swap_interval=10, max_steps=None):
        # calculate max_steps if not provided
        if not max_steps:
            max_steps = 10 * n_samples + burn_in_steps
        else:
            max_steps = max_steps + burn_in_steps
            
        # burn-in phase for each samplers
        for chain in self.chains:
            if not hasattr(chain, '_burned_in'):
                l, r = start_value
                chain.burn_in(burn_in_steps, np.random.uniform(l, r))

        samples, steps = np.array([]), 0
        while len(samples) < n_samples:
            # run all th chains for swap_interval steps     
            for i, chain in enumerate(self.chains):
                s = chain.run(swap_interval)
                # Collect samples from the coldest chain (T=1)
                if chain.temperature == 1:
                    samples = np.concatenate([samples, s])

            # after swap_interval steps, swap states between chains
            self.swap_chains()

            # check if max_iter is reached, if so exit from iteration
            if steps > max_steps:
                print("Processed stop because maximum steps is reached")
                break
                        
        
        self.samples = np.concatenate([self.samples, samples])
        # return samples
        return samples

