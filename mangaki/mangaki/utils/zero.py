class MangakiZero(object):
    def __init__(self, NB_COMPONENTS=10, NB_ITERATIONS=10):
        pass

    def set_parameters(self, nb_users, nb_works):
        pass

    def fit(self, X, y):
        pass

    def predict(self, X):
        return [0] * len(X)

    def __str__(self):
        return '[ZERO]'

    def get_shortname(self):
        return 'zero'
