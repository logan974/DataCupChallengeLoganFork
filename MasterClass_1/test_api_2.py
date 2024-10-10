import unittest

# Variables globales à tester
id_list = None
id_titles = None

# Classe de tests pour vérifier les résultats de l'API articles
class TestArticlesAPI(unittest.TestCase):
    def test_id_list(self):
        expected_id_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12]
        # Comparer les deux listes sans tenir compte de l'ordre
        self.assertCountEqual(id_list, expected_id_list, "La liste des IDs n'est pas correcte")

    def test_id_titles(self):
        expected_id_titles = [
            'Comment jongler avec des baguettes magiques',
            'Le guide ultime du sabre laser',
            'Le secret du sourire de la Joconde',
            'Comment survivre à une apocalypse zombie',
            'Construire son armure en cave',
            'Les meilleures pizzas pour tortues ninja',
            'Faire ses courses en Batmobile',
            "L'art du camouflage en forêt",
            'Les vertus du miel magique',
            'Pourquoi les aliens adorent les vélos',
            'Article de la masterclass'

        ]
        # Comparer les deux listes sans tenir compte de l'ordre
        self.assertCountEqual(id_titles, expected_id_titles, "La liste des titres n'est pas correcte")
