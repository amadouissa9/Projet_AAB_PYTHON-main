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
            print(f'Mr/Mme {nom} {prenom} a été(e) ajouté(e) avec succès!')
        except Exception as e:
            print("Erreur d'insertion !",e)
    
    def client_existe(self, email):
        # Vérifie si un utilisateur avec l'email donné existe dans la base de données
        sql = "SELECT COUNT(*) FROM utilisateur WHERE Email_util = %s"
        self.cursor.execute(sql, (email,))
        count = self.cursor.fetchone()[0]
        return count > 0
    
    @classmethod
    def modifier_utilisateur(self, email, id_utilisateur, nouveau_nom, nouveau_prenom, nouveau_sexe):
        try:
            # Vérification de l'existence de l'utilisateur
            utilisateur_existe = self.client_existe(email)
            if not utilisateur_existe:
                print("L'utilisateur avec cet email n'existe pas.")
                return

            # L'utilisateur existe, procéder à la modification
            sql = "UPDATE utilisateur SET ID_utilisateur = %s, Nom_util = %s, Prenom_util = %s, Sexe_util = %s WHERE Email_util = %s"
            values = (id_utilisateur, nouveau_nom, nouveau_prenom, nouveau_sexe, email)
            self.cursor.execute(sql, values)
            self.connection.commit()
            print("Utilisateur modifié avec succès !")
        except Exception as err:
            print(f"Erreur lors de la modification de l'utilisateur : {err}")
