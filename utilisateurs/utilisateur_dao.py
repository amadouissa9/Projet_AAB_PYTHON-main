import database  
class UtilisateurDao:
    connecte= database.connexion()
    cursor= connecte.cursor()

    @classmethod 
    def add_utilisateur(cls,nom, prenom, age, email,password, role ):
        try:
            sql = "INSERT INTO utilisateur(Nom_util, Prenom_util, Age_util, Email_util, Password_util, 	Role) VALUES(%s, %s, %s, %s, %s, %s)"
            params =(nom, prenom, age, email,password, role)
            cls.cursor.execute(sql, params)
            cls.connecte.commit()
            print(f'Mr/Mme {nom, prenom} a été(e) ajouté(e) avec succès!')
        except Exception as e:
            print("Erreur d'insertion !",e)
