from utilisateurs.utilisateur_dao import UtilisateurDao
#from utilisateur import Utilisateur

utilisateur_dao = UtilisateurDao()
message = utilisateur_dao.add_utilisateur('armel', 'joel', '40', 'bij@tes.com', '12345', 'Admin')
#message = utilisateur_dao.modifier_utilisateur('bij@test.com')
print(message)