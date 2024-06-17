# fuzzy_logic.py

from rules import FuzzyRules

class FuzzyLogicController:
    def __init__(self):
        self.rules = FuzzyRules()

    def defuzzify(self, output_set, output_variable):
        numerator = sum(
            value * (self.rules.get_output_range(output_variable, term)[0] + self.rules.get_output_range(output_variable, term)[1]) / 2
            for value, term in output_set
        )
        denominator = sum(value for value, term in output_set)
        return numerator / denominator if denominator != 0 else 0

    def infer(self, temp_actual, temp_desired):
        rule_results = self.rules.evaluate_rules(temp_actual, temp_desired)
        
        comp_activations = [(activation, comp_term) for activation, comp_term, _ in rule_results]
        fan_activations = [(activation, fan_term) for activation, _, fan_term in rule_results]

        comp_output = self.defuzzify(comp_activations, 'comp_power')
        fan_output = self.defuzzify(fan_activations, 'fan_speed')

        return comp_output, fan_output
