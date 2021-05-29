import requests

class Bourreau:

    def __init__(self, numeroDeTournes = 5, indices = "", indicesCorrecte = []):
        # api pour un mot aleatoire
        reponse = requests.get("https://random-words-api.vercel.app/word").json()
        self.mot = reponse[0]["word"]
        self.numeroDeTournes = numeroDeTournes
        self.indices = indices
        self.indicesCorrecte = []
        for i in range(len(self.mot)):
            self.indicesCorrecte.append("_")

    def getMotCommeListe(self):
        return list(self.mot.lower())

    def getNumeroDeTournes(self):
        return self.numeroDeTournes

    def getIndices(self):
        return self.indices

    def getIndicesCorrecte(self):
        return self.indicesCorrecte

    def setNumeroDeTournes(self, numeroDeTournes):
        self.numeroDeTournes = numeroDeTournes

    def setIndices(self, indices):
        self.indices = indices

    def setIndicesCorrecte(self, indicesCorrecte):
        self.indicesCorrecte = ''.join(indicesCorrecte)

    def getIndexesDeIndiceDansMot(self, indice):
        listeDesIndexes = []
        for indexe, lettre in enumerate(self.getMotCommeListe()):
            if lettre == indice:
                listeDesIndexes.append(indexe)
        return listeDesIndexes

    def start(self):
        self.devine()

    def devine(self, indice = ""):
        if not isinstance(indice, str):
            indice = indice.get()

        if len(indice) < 1:
            return

        bourreau = self
        # recever le mot du jeu
        mot = bourreau.getMotCommeListe()
        # les indices du joueur
        indices = bourreau.getIndices()
        # les indices correctes du joueur
        indices_correcte = list(bourreau.getIndicesCorrecte())
        # combien de fois le joueur peut joueur sans gagnant
        numero_de_tournes = bourreau.getNumeroDeTournes()

        if numero_de_tournes > 0:
            if len(indice) > 1:
                return print("Devinez seulement une seule lettre.")

            if indice in indices:
                return print("Vous avez deja utilisez cette lettre.")

            # additionne l'indice du joueur avec les indices
            bourreau.setIndices(indices + indice)

            # si l'indice n'existe pas dans le mot,
            # promptez le joueur de reessayez ou
            # si le joueur n'a plus de tournes, on dit qu'il a perdu
            if indice not in mot:
                bourreau.setNumeroDeTournes(numero_de_tournes - 1)
                numero_de_tournes = bourreau.getNumeroDeTournes()

                if numero_de_tournes == 0:
                    print("Tu as perdu.\n")
                    print("Le mot correcte est: " + ''.join(mot) + "\n")
                    return
                else:
                    print("Reessayez")
                    return

            else:
                # comptez comment de fois l'indice se trouve dans le mot
                # et puis additionnez l'indice dans la liste
                # des correctes indices dans le correcte indexe
                # comme se trouve dans le mot originale
                indexes_du_correcte_indice = bourreau.getIndexesDeIndiceDansMot(indice)
                for correcte_indexe in indexes_du_correcte_indice:
                    indices_correcte[correcte_indexe] = indice
                    bourreau.setIndicesCorrecte(indices_correcte)

                print(''.join(indices_correcte))

            # si le mot est le meme que les characteres de mots le joueur a devine
            # on dit qu'il gagne
            if indices_correcte == mot:
                print("Tu gagne!\n")
        else:
            print("Tu as perdu")

bourreau = Bourreau()
bourreau.start()
while bourreau.getNumeroDeTournes() > 0:
    ind = input("devine: ")
    bourreau.devine(ind)