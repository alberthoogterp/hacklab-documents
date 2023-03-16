Zoektocht = {'dict' : {'dict' : {'dict' : {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 
            'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", 
            ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': 
            {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}, 'list': 
            ["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]], 
            'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': 
            {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 
             'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 
             'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': 
             {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}}, 
             'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 
             'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'dict' : 
            {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': 
            [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 
            'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': 
            {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}, 'list': 
            ["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]], 
            'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : 
            {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': 
            [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 
            'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'dict' : 
            {'Deze': "Het antwoord", 'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 
            'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 
            'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': 
            {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}, 'list': 
            ["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]], 
            'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : 
            {'Deze': "Het andwo0rdt", 'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 
            'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 
            'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': 
            {'Deze': "Het andw00rd", 'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}}}}}, 
            'list': ["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]], 
            'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : 
            {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': 
            [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 
            'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': 
            {'Deze': "Het andwoord", 'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}}

antwoord = Zoektocht["dict"]['nou nog eentje dan']["nou nog eentje dan"]["nou nog eentje dan"]["dict"]["dict"]['Deze']
print(antwoord)
