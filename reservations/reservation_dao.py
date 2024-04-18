import database
class reservationDao:
    connexion = database.connexion()
    cursor = connexion.cursor()

    @classmethod
    def recupere_Nom_event(cls):
        sql = """
                SELECT evenement.Nom_event,  reservation.Nom_Event 
                FROM evenement 
                INNER JOIN reservation 
                ON evenement.Nom_event = reservation.Nom_Event
              """
        cls.cursor.execute(sql)
        nom_event = cls.cursor.fetchone()
        if nom_event:
            return nom_event[0]
        else:
            return "le Nom n'existe pas "
        
    @classmethod
    def recupere_Nom_utilisateur(cls):
        sql = """
                SELECT utilisateur.Nom_util, reservation.Nom_util 
                FROM utilisateur 
                INNER JOIN reservation 
                ON utilisateur.Nom_util = reservation.Nom_util
            """
        cls.cursor.execute(sql)
        nom_util = cls.cursor.fetchone()
        if nom_util:
            return nom_util[0]
        else:
            return "Le nom n'existe pas."

        
    def reservation_place(cls,nom_event, nom_util, place):
        try:
            #nom_event = cls.recupere_Nom_event()
            #nom_util = cls.recupere_Nom_utilisateur()
            sql = "INSERT INTO reservation (Nom_Event, Nom_util, Nombreplaces_event) VALUES (%s, %s, %s)"
            valeurs = (nom_event, nom_util, place)
            cls.cursor.execute(sql, valeurs)
            cls.connexion.commit()
            sms = "La réservation a été effectuée avec succès !"
        except Exception as e:
            sms = f"Une erreur s'est produite lors de votre réservation : {e}"
        print(sms)

