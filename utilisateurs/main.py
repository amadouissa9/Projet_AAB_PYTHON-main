import database

class UtilisateurDao:
    connect= database.connexion()
    cursor= connect.cursor()

    @classmethod 
    def add_utilisateur(cls,nom, prenom, age, email, password, role):
        try:
            sql = "INSERT INTO utilisateur(Nom_util, Prenom_util, Age_util, Email_util, Password_util, Role_util) VALUES(%s, %s, %s, %s, %s, %s)"
            params =(nom, prenom, age, email, password, role)
            cls.cursor.execute(sql, params)
            cls.connect.commit()
            print(f'Mr/Mme {nom} {prenom} a été(e) ajouté(e) avec succès!')
        except Exception as e:
            print("Erreur d'insertion :", e)

    @classmethod
    def show_menu(cls):
        while True:
            print("===== MENU UTILISATEUR =====")
            print("1. Ajouter un utilisateur")
            print("2. Quitter")
            choix = input("Choisissez une option : ")

            if choix == "1":
                nom = input("Nom : ")
                prenom = input("Prenom : ")
                age = input("Age : ")
                email = input("Email : ")
                password = input("Mot de passe : ")
                role = input("Role : ")
                cls.add_utilisateur(nom, prenom, age, email, password, role)
            elif choix == "2":
                print("Au revoir!")
                break
            else:
                print("Option invalide, veuillez choisir à nouveau.")

# Exemple d'utilisation :
if __name__ == "__main__":
    UtilisateurDao.show_menu()
