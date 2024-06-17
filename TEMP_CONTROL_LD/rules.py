# rules.py

class FuzzyRules:
    def __init__(self):
        self.membership_functions = {
            'temperature_actual': {
                'low': lambda x: max(0, min(1, (20 - x) / 20)),
                'medium': lambda x: max(0, min((x - 10) / 10, (30 - x) / 10)),
                'high': lambda x: max(0, min((x - 20) / 10, 1))
            },
            'temperature_desired': {
                'low': lambda x: max(0, min(1, (20 - x) / 5)),
                'medium': lambda x: max(0, min((x - 20) / 5, (25 - x) / 5)),
                'high': lambda x: max(0, min((x - 25) / 5, 1))
            }
        }

        self.output_ranges = {
            'comp_power': {
                'off': [0, 0],
                'low': [0, 25],
                'medium': [25, 75],
                'high': [75, 100]
            },
            'fan_speed': {
                'off': [0, 0],
                'low': [0, 25],
                'medium': [25, 75],
                'high': [75, 100]
            }
        }

        self.rules = [
            # Casos en los que la temperatura deseada es mayor o igual a la actual
            (('low', 'high'), ('off', 'low')),
            (('medium', 'high'), ('off', 'low')),
            (('high', 'high'), ('off', 'low')),
            (('low', 'medium'), ('off', 'low')),
            (('medium', 'medium'), ('off', 'low')),
            (('high', 'medium'), ('off', 'low')),
            (('low', 'low'), ('off', 'low')),
            (('medium', 'low'), ('off', 'low')),
            (('high', 'low'), ('off', 'low')),
            # Casos en los que la temperatura actual es mayor que la deseada
            (('high', 'medium'), ('high', 'high')),
            (('high', 'low'), ('high', 'high')),
            (('medium', 'low'), ('medium', 'medium')),
            (('medium', 'medium'), ('medium', 'medium')),
            (('low', 'medium'), ('low', 'medium')),
        ]

    def get_membership_values(self, variable, value):
        return {term: func(value) for term, func in self.membership_functions[variable].items()}

    def evaluate_rules(self, temp_actual, temp_desired):
        temp_actual_mf = self.get_membership_values('temperature_actual', temp_actual)
        temp_desired_mf = self.get_membership_values('temperature_desired', temp_desired)

        rule_results = []
        for (actual_term, desired_term), (comp_term, fan_term) in self.rules:
            activation = min(temp_actual_mf[actual_term], temp_desired_mf[desired_term])
            rule_results.append((activation, comp_term, fan_term))

        return rule_results

    def get_output_range(self, variable, term):
        return self.output_ranges[variable][term]
