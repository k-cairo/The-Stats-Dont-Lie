from datetime import date, timedelta, datetime

today = datetime.today().strftime("%d-%m-%Y")
tomorrow = (date.today() + timedelta(days=1)).strftime("%d-%m-%Y")
j2 = (date.today() + timedelta(days=2)).strftime("%d-%m-%Y")
day_list = (today, tomorrow, j2)

CARDS = "/cards"
CORNERS = "/corners"
LEAGUES_URLS = {
    "Australia": "https://www.thestatsdontlie.com/football/rest-of-the-world/australia/a-league",
    "Austria": "https://www.thestatsdontlie.com/football/europe/austria/bundesliga",
    "Belgium": "https://www.thestatsdontlie.com/football/europe/belgium/pro-league",
    "Brazil": "https://www.thestatsdontlie.com/football/n-s-america/brazil/serie-a",
    "China": "https://www.thestatsdontlie.com/football/rest-of-the-world/china/super-league",
    "Croatia": "https://www.thestatsdontlie.com/football/europe/croatia/1-hnl",
    "Czech_Republic": "https://www.thestatsdontlie.com/football/europe/czech-republic/1-liga",
    "Denmark": "https://www.thestatsdontlie.com/football/europe/denmark/superliga",
    "England1": "https://www.thestatsdontlie.com/football/uk-ireland/england/premier-league",
    "England2": "https://www.thestatsdontlie.com/football/uk-ireland/england/championship",
    "France1": "https://www.thestatsdontlie.com/football/europe/france/ligue-1",
    "Germany1": "https://www.thestatsdontlie.com/football/europe/germany/bundesliga",
    "Germany2": "https://www.thestatsdontlie.com/football/europe/germany/2-bundesliga",
    "Holland1": "https://www.thestatsdontlie.com/football/europe/holland/eredivisie",
    "Holland2": "https://www.thestatsdontlie.com/football/europe/holland/eerste-divisie",
    "Italy": "https://www.thestatsdontlie.com/football/europe/italy/serie-a",
    "Poland": "https://www.thestatsdontlie.com/football/europe/poland/ekstraklasa",
    "Portugal": "https://www.thestatsdontlie.com/football/europe/portugal/primeira-liga",
    "Scotland": "https://www.thestatsdontlie.com/football/uk-ireland/scotland/premiership",
    "Spain1": "https://www.thestatsdontlie.com/football/europe/spain/la-liga",
    "Sweden": "https://www.thestatsdontlie.com/football/europe/sweden/allsvenskan",
    "Turkey": "https://www.thestatsdontlie.com/football/europe/turkey/super-lig",
    "USA": "https://www.thestatsdontlie.com/football/n-s-america/usa/mls"
}

TEAMS_IN_CHAMPIONSHIP = {
    "Australia": 12, "Austria": 12, "Belgium": 18, "Brazil": 20, "China": 16, "Croatia": 10, "Czech_Republic": 16,
    "Denmark": 12, "England1": 20, "England2": 24, "France1": 20, "Germany1": 18,
    "Germany2": 18, "Holland1": 18, "Holland2": 20, "Italy": 20, "Poland": 18, "Portugal": 18, "Scotland": 12,
    "Spain1": 20, "Sweden": 16, "Turkey": 20, "USA": 27
}

##### FOR GET ALL MATCHS #####
LIST_CHAMPIONSHIP = [
    "Australie : A-League", "Autriche : Bundesliga", "Belgique : Pro League", "Brésil : Série A",
    "Chine : Super League", "Croatie : 1. HNL", "République Tchèque : Ligue Tchèque", "Danemark : Superligaen",
    "Angleterre : Premier League", "Angleterre : League Championship", "France : Ligue 1",
    "Allemagne : Bundesliga", "Allemagne : 2. Bundesliga", "Pays-Bas : Eredivisie",
    "Pays-Bas : Eerste Divisie", "Italie : Serie A", "Pologne : Ekstraklasa", "Portugal : Liga Sagres",
    "Écosse : Premier League", "Espagne : Liga BBVA", "Suède : Allsvenskan",
    "Turquie : Süper Lig", "Etats-Unis : Major League Soccer"]

#### CONVERSION #####
CONVERSION_LIST = {
    "Australie : A-League": "Australia",
    "Autriche : Bundesliga": "Austria",
    "Belgique : Pro League": "Belgium",
    "Brésil : Série A": "Brazil",
    "Chine : Super League": "China",
    "Croatie : 1. HNL": "Croatia",
    "République Tchèque : Ligue Tchèque": "Czech_Republic",
    "Danemark : Superligaen": "Denmark",
    "Angleterre : Premier League": "England1",
    "Angleterre : League Championship": "England2",
    "France : Ligue 1": "France1",
    "Allemagne : Bundesliga": "Germany1",
    "Allemagne : 2. Bundesliga": "Germany2",
    "Pays-Bas : Eredivisie": "Holland1",
    "Pays-Bas : Eerste Divisie": "Holland2",
    "Italie : Serie A": "Italy",
    "Pologne : Ekstraklasa": "Poland",
    "Portugal : Liga Sagres": "Portugal",
    "Écosse : Premier League": "Scotland",
    "Espagne : Liga BBVA": "Spain1",
    "Suède : Allsvenskan": "Sweden",
    "Turquie : Süper Lig": "Turkey",
    "Etats-Unis : Major League Soccer": "USA"
}

NEW_CONVERSION_LIST = {
    "Australie : A-League": "Australie - A-League",
    "Autriche : Bundesliga": "Autriche - Bundesliga",
    "Belgique : Pro League": "Belgique - Pro League",
    "Brésil : Série A": "Brésil - Série A",
    "Chine : Super League": "Chine - Super League",
    "Croatie : 1. HNL": "Croatie - 1. HNL",
    "République Tchèque : Ligue Tchèque": "République Tchèque - Ligue Tchèque",
    "Danemark : Superligaen": "Danemark - Superligaen",
    "Angleterre : Premier League": "Angleterre - Premier League",
    "Angleterre : League Championship": "Angleterre - League Championship",
    "France : Ligue 1": "France - Ligue 1",
    "Allemagne : Bundesliga": "Allemagne - Bundesliga",
    "Allemagne : 2. Bundesliga": "Allemagne - 2. Bundesliga",
    "Pays-Bas : Eredivisie": "Pays-Bas - Eredivisie",
    "Pays-Bas : Eerste Divisie": "Pays-Bas - Eerste Divisie",
    "Italie : Serie A": "Italie - Serie A",
    "Pologne : Ekstraklasa": "Pologne - Ekstraklasa",
    "Portugal : Liga Sagres": "Portugal - Liga Sagres",
    "Écosse : Premier League": "Écosse - Premier League",
    "Espagne : Liga BBVA": "Espagne - Liga BBVA",
    "Suède : Allsvenskan": "Suède - Allsvenskan",
    "Turquie : Süper Lig": "Turquie - Süper Lig",
    "Etats-Unis : Major League Soccer": "Etats-Unis - Major League Soccer"
}

LOGO_LIST = {
    "Australia": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxISEhUTEhQWFRUXFxoWGBUYGB0eGBYXGhcXGhkWGhkYHSggGRopGxodITEhJTUrLi4uIx8zODMsNygtLisBCgoKDg0OGxAQGy4mICYyNTUyNjItLS8tLzItLS4tLTctLy0uOC0vLS0tLS8vLS0tLS0tLS0vLS0vLS0vLS0uLf/AABEIAJYAlgMBIgACEQEDEQH/xAAcAAEAAwEBAQEBAAAAAAAAAAAABQYHBAMCAQj/xABDEAACAQIDBQMIBwYEBwAAAAABAgMAEQQFIQYSMUFRE2FxIkJSgZGhscEHFDJicpLRIzOCosLhU7PS8BYkJURzdeL/xAAaAQACAwEBAAAAAAAAAAAAAAAABQMEBgIB/8QAMhEAAQMCAgcHBQADAQAAAAAAAQACAwQRITEFEkFRcYHREzJhobHh8CJCkcHxFCNSM//aAAwDAQACEQMRAD8A3GlKUISlKUISo3Oc5gwkfaTyLGvK/Fj0VRqx7hUbtZtMmDSws8rDyE/qbovx94xPO8XNipDJM5Zj14AdFHADuFVpqlrDqjNMKTR7pxruwb5nh1/C0N/pjwpkCJDJYmwdyFHiQLkCrNle18MhCyAxk6Ak3X83L11/PU+D+I+NaE1UJqyRhDgeSbN0XTuaW2t43N+nktqrHszUrLIpJ8l2Gp6MRV12HzYyIYnN2jFweqcLeo/EVWNroNzFSjqQ35gD8b0VzxLCyQb/ANeyh0bGYKiSF275+bqNhxkq/Ydl8GI+FaFsVjXlgPaMWZXIuTc2spGvtrN6uf0c4j97H3Kw9VwfiKr0EhEwF81b0rGHUznWxFj5qxYnOo4pezlulwCrn7DDx5G+mtSaOCLg3B4EVDbVZZ28Bt9tPKXv6r6x77VTcg2hkw5s12i5r0716Hu4GmT6owy6sndOR+bv6k8VE2oh14u8Mxv4br/i98lp1K5sHi0lQOh3lPA/I9DXTV0EEXCWkEGxSlKV6vEpSlCEpSlCEqKz7Nlw0JkbU8EX0m5Dw5mpWsq2wzX6xObH9ml1Xoeres+61Vquo7FlxmcldoKT/Ilse6M+nP0uq7mM7zSNJId5mNyfkOgHC1R8kNSTJVn2X2PM1pZrrFxC8Gf9F7+fLrSaIPkdZuJWmmkjgZrOwA+WCouGyl5TdUJVbF2A0UXHE8BU6au+2cscECYeIBQxuVHor18Wtr3GqRXlW3UeGXvb9+1l5RymaPtLWBy4D3up3YqQri4/vBlPhuk/ECpH6Q8NZ45OqlT4qb/BvdUfsRHvYtD6IZv5SPiatu2mD7TDMRxQhx4cD7jf1VYgjL6Rw8bjlb3VGolEekIzvFjzJt+lmdTmxuL7PFLfg90P8XD+a1QlfSMQQRoQbg94pfG8scHDYm0sYkYWHaLLaayvarAdjO4A8lvLXwPL1G4rR8rxgmiSQecoJ7jzHqNxVe+kHCXiSUcUbdP4W/uB7ae10Ylh1hsx5bfJZjRkpiqdQ7cDx2eeHNV7ZfPDh5LMf2THyh0Ppjv69R6q0xGBFxqDqD1rEy1aDsHm/aRmFj5UfDvT+x08CKq6OqCD2Ry2dFd0vSAjt2jHb15bfDgrdSlKcLPpSlKEJSlKEKG2px3Y4Z2H2m8hfFuPuuaysirv9ImI0ij/ABMfcB86i9kci7d99x+yQ6/eb0fDmf70jrNaao7Nuz+laXR+pT0nav24/oey6tkdmN+0848niiHzvvH7vdz8ON8kkCgk6AC5PIAV9AW0FUvbjO/+3jP/AJCPcnzPq76YWjo4rj+n5+AlV5dITgH2aPm3afKt59mRxE7Py4KOijh+viTUdSvuCIswVRcsQAOpJsKz7nFziTmVq2taxoaMAP0rn9HmD0kmPOyD4t8quEqBlKkXBBBHUHQ1zZRgRBCkY80anqx1J9td1aWmi7KINPP1WNrJ+3mc8ZbOAyWPZngzDK8Z4qbeI5H1ixrlq8be5XcCdRw8l/DzW9unsqj1n6mHspC3Zs4fMFq6OoE8Ift28dvXmrnsBmVt7DsePlp4+cPZr7as2f4btMNMv3CR4r5Q94rK8PO0bK6mzKQQe8VqeS5mmJiDjjwdfRbmPCmdBMJGGF3we3ok2lIDDKKhu/HiOvqscZ679nMz+r4mOS9l3rN+FtD+vqqLxp3HZfRYj2G1cUk1LmAtIIzCePDXgtOR/a/oilRWzOL7XCQScSY1v4gWPvBqVrSA3F1inNLXFp2JSlK9XKUpShCpG2OEabFwxLxKD1eU9z4AC9WzL8GsMaxpwUW8TzJr6+qL2naW8vc3L/dvf41AbSbTrBeOOzS8zyTx6t3e3pVPVZAXzPOfpuHqmBfJVNjgjHdHntJ8BkvTanaAYddxDeVh+Qeke/oPX45wzEm51J1J619SysxLMSSTck8Sa+aTVNQ6d1zlsWio6RlMzVGZzO/23JVz2GybXt3Gg0jB5nm/yHr6VC7M5I2Ik1uI11dv6R3n3VpsUYUBVFgBYAcABwFWtH02se1dkMuPt68FQ0tW6jexZmc/AbuJ9OK9aUpTtZxeM0SupVhdSLEHmDWWZ/lLYeUqdVOqN1X9RwP961mo/N8sTERlH8Vbmp6iqlZTduzDvDJX6Cs/xn49059VklSOQ5s+GkDrqp0dfSH6jka+M2yqTDvuOPBhwI6g/KuGs+C+N+4haohkzLZtI5H55KBzac9q5Itdi1u4kkeNRM+Kq2Y3BpKu6/qYcV8P0qs4jZbEFrIyMCdDex/L18KtRyMPeNlw5hGAW4fRk+9lmHPc/wDmyVaah9lMq+qYSDD8SiAMerG7MfzE1MU/YLNAWOncHSucNpPqlKUrpRJSlKEKD2ulkTDM0RKkEXI47p0Njy1I1rMTWyTwh1ZG1VgVI7iLGslzTAtBK8bcQdD1HI+yk2k4zrB+zLh/VodCytLHR7c+I9v2uSpPIMkfEvZdEH2m5AdB1PdXTs9s6+IO8bpGOJ5nuXqe/lVtzXNIcDEqIo3reSn9bHj8zVenpQW9rLg31+eat1VYQ7sYMXn8Dj8wzKlcPBFh4gosiLzJA9ZJ51G4vazCpoGLn7g+ZsKz7MMylnbekcnoOQ8BwFclTyaSOUbbDx6KtFoZvemcSTu65nyV4k27XzYSfFgPgDXj/wAen/A/n/8AmqbSq5rqj/ryHRWxoylH2ebuqvMe3a+dCR4MD8QK78PtjhW4l0/Ev+kms3pXQ0hONoPLpZcO0TTHIEcD1utXM2GxK7m9HID5txfxtxB76r2P2GF7wyWHovy/iH6VSgalcBtFiYeEhYei3lD36j1VI6sil/8AZnMfP2om6Pmp8aeTkRh85KRXYjEX1aMDrvH/AE1YMi2Wjw5EjnfkHA28lT1A699ceW7bI2kyFD6S6r7OI99WnC4lJFDowZTwIq3TQ0pOtHiRvOXJUK2orWt1JRYHcMDzXvSlKYpQlKUoQlKUoQlRWY5JDO6PILlOnnDo3UX1qVpXLmNeLOFwu2SOjdrMNivBisaE2AVQTYcgByFZLmWNaaVpG4sb+A5DwA0rVsyiLQyqvFkZR4lSBWE57nS4chAN6Qi9jwUdW/Slekg9xYxvj85D1TvQoYA95zwHLH1Popa1d+FyfESAFInIPA20PgTpVDXHyyfbYnuGg9gq3bNbV4jDAKG34/8ADfUD8J4r8O6qTYGA/wCwm3h7ptLLJq/6gL+Pz1U8mx+LPmAeLL8ia+n2NxXoqf4h86sWV7aYaXR7xN97VfUw+dqsWHnRxdGVh1Ugj3VfjoaZ4+lxPMdEml0lWRGz2Acj63ssxm2Zxa8YmP4SD8DUbPhXQ2dGU/eBHxrZq+JIwRYgEdDwofotn2uI42PRDNNv+5gPAket1i1ftahjtmcNLxj3D1TT3cPdVZzPYmRLmFhIPROjfofdVKWgmZiBfh0TGHSlPJgTqnx6quYHCNLIsaC7MbD5k9wGta1gMIsUaxrwUW8ep8SdahdlMh+rrvuP2rD8i+j49f8Ad7JTKgpuybrOzPkPmKUaUrBM/UYfpb5n2yHPelKUq+lSUpShCUpShCUpShCVkn0nfR9JLJ9bwi75I/aRD7Vx56Dzu9ePS/LW6Vw9gcLFTQTvhfrN/q/mHCqQbEEEaEHQg9CKmMPW25vs3hcTrNEpb0xo/wCYan11WMX9GyjWGYgei63/AJlt8KXTUkn24p7BpSF3fuPMflUaOu3DTshujFT1BIPuqebYLFLwaNvBj8xRdi8V6KfmFUHU01+6VeFZTkd8fkLyw+1GLThKWH3gD7yL13x7b4gcVjPip+TV+wbDzn7Txr6yT8LVNYLYuBdZGaTu+yvu199TxxVuwkcT/T5KnNPo8YkNPAfPVceA2rxMzbiQKx7r2HeTfQVboN/dHabu9z3b29V9a/MLhkjXdRQo6AWroprBG9g+t2sfL5xSOpmjkP8ArYGjz6cglKUqdVkpSlCEpSlCEpSlCEqLzbP8LhbdvMiFvsoTd2/Ci3ZvUK6M0kkWGVoV35FjcxqeDOFJVfWbCsj2o2hhwGUxzYd9/G45bPiT++3rDtyW4puE7gQW3CRYaUIV3wX0j4GdmXDjETlPtmLDSsE/F5OnA+ypbL9qcJM4jWQpIeEcqPE5PQLKqlj3C9ZT9Fs+bYbAtFhcsB3naXt5pOzD3AA/ZtZm0FgQQPjXNsAMXn2LbEZi3aYXDg2itaHtWUhVCjjYEsW1I8nXWhC3qvFJ0ILBlKi9yCLC3G5qu7A4lngkG+ZYknljw8zG5lgUgK2954DbyB/OCg63vWT7OYvMFyjHpBhYpMKTiu0laXddQUIchOdl1HWhC3lMSjGyupJG9YEE7vXw76/HxUakguoIFyCwuB1PQaisbmyx4spy7NsKQMTg4VLX4SwEkNG3UC59RbnavHOMkdNn8bj8QQ+Kxxhnkb0Y2niaONegCkG3gPNFCFtrzKLXYC5sLkak8AOtebY6IEgyICOILC499Zj9IOKjePJlSRGIxuGuFYEjQcgeFc2zWyOCx+Y5scXCJSmJAW7Otgwcn7DDoKELWWxSABi6hTwJYWPgedIcVG5srqx6BgfhX884WBJMqyyKXWI5oY2DNYdmWIYXv5IsTr41bsNk2Cwef4FcCFRHgnLhJCwJCPa92PT3d1CFqrY6IEgyICNCCwuPfXoMQhIG8t2F1FxcjqOor+ZMrwML5XLK+VzzS7sp+vB23FIJs5F7ELz011q/bPD/AKhkH/rT/ktQhbHSlKEJSlKEJSlKEJVL2j2Ty8zpimP1bE7xZZk3blrasyOrI514kX4a1dKoO1THE4xIFI8nybngGOrH2WHqqvUzGJl2i5JsOatUdOJ5LONmgEk7gF0SZNjsTE6rmu9G4KFlw0Yex0YBgwANudr9LV45VsBh8JhxFNiJpYI7kxEiOFrm5MixAGXX0yw4C1fewmP3RNE19AZAOemjAd/Cutc9+tYbE3j3N1DzuCDfnbjpUbKtrowT3iDhwzU8uj3tlc0d0FuOGTrWU/lmLhdd2FlKoAtlFgotoAOQsKiVweXYaKXCWjjjk3jJFc+V2gs19b6iuP6O/sS/iX4GofbMgY03FxZLi9riwuL8qjdVvFO2WwuTy29FIzR7HVboLmwHPZ1VkhTLngGBXcaEr2YhBaxW/wBm/H319YmPL5oRgX7NorJEIbm1oyu4oIN9Co58qg8pnw6pNiI4WjaJbKxct5b3UCxAqAWB0RJweLkDqCtjf3+6onV72gGwOZwvle2221Tt0XE5xF3C1hjbvHHZfC1lccHsBlWHdZ0wsaNGQ6uWYhSNQ3lMRcHW9d2VjARSzNA0SyTMHlIb94wvY6m3M8Kru2mZmQQKpsjIJSORLEix8LGv3McrwOHKJI8pcAMxWxBB5a8KllrHBzgwCwtck2zysoYdHNLGmQu1nXsAL2tndd+Y7M5RHCmFmijWJWMqRlnsGa4LCxvX1gdmspy+RZo4Y4XYEK92JsQN628TbQ8R1qF2tmjk+rtECE7MhQeICsV5k9Kkdvv3eG/i+CV4+scBIQB9NreN16zRzS6Jrifq1r5YavzFSCYPLIcMcGBGkEik9ldrMsmpN7318a/cBhMtM2HaERmWCMxQEFrpHukFRc2Pk343NVbaU64a+o+rRfOpjZJsO857OFo2VWYMXLDkpFrDrXjax5m7PDPx8l1Jo2NkBk+o4HdYbr7fxdXilKUySZKUpQhKUpQhecz7qk9AT7BWc5Rk5xc0hd93ixIFySWHXlqaUqjVMD5Y2uyx/SaUMjo6eaRmBFsV9QYM4PGqFbeCso6Eh7A+41c88gAw0wUAXQnQW166UpXFO0NZK0ZY+nspapxe+B7syBf8jqVn+ExGIw91jk3QdTbnbxFde0aOcQr3G9uRtf726Dfh1pSljSTERfd+02cAJgQBc3vgMcs12Z3NNJhYA77xctIx4aLoF0HQ38a8sXsmEw3bCS53Vbdtpra4vx50pVvs2yPfr42aLfhU3yvhZGI8LvN7Af8AZHovzBZScThrXAeEndJ4FG13Tpe4a5HjXIgxOIYYZpAQpA17tB5QXePHnX7SoZWgCO33AA4nFTxOLnSXsdU4YDC+JtzU3nmzP/LRhXBaENcnQMGO8bW4WJ0qDwWFnxrrG0twg0LeaOdrDU6c6UqephYJmtGRAvicbKvRzvdTvecwTbAYXxPqu3a7BETIEIAjiRVvxst7cq7Nm8zxUk6LJJvIQ1xYcl05daUri5bUmxI+obV3qtfRguAJ1DmBuV2pSlO1mkpSlCF//9k=",
    "Austria": "https://upload.wikimedia.org/wikipedia/fr/a/a7/Austrian_Football_Bundesliga.png",
    "Belgium": "https://www.tac-tyk.fr/wp-content/uploads/2020/05/Jupiler-1.png",
    "Brazil": "https://b.fssta.com/uploads/application/soccer/competition-logos/BrazilSerieA.png",
    "China": "https://www.thesportsdb.com/images/media/league/badge/c7evs21534799383.png",
    "Croatia": "https://bi.im-g.pl/ldpic/league/logo/league_252.png",
    "Czech_Republic": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnGonoLVQuk5X3ak90mI3oNoyfqLjlUTVAqH-adJS3D7yR8v-mNvpZ9nUgmneRhc5PX14&usqp=CAU",
    "Denmark": "https://1.bp.blogspot.com/-WrLIOHaKz5I/YLJZLrCSuxI/AAAAAAAAoS0/8Z7trPKZf5cha_Ufu8gRfpqOahoK_qIqACLcBGAsYHQ/s225/download%2B%25281%2529.png",
    "England1": "https://www.xalimasn.com/wp-content/uploads/2018/01/premi.png",
    "England2": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyCaV9vPzMzUaSTmWLcETkXFm-ABzHB3kB9UMxn01n1fgV_Hx-GdJ1e3rcmIACjxJvmm0&usqp=CAU",
    "France1": "https://leblogdenins.com/wp-content/uploads/2016/07/ligue1.png",
    "Germany1": "https://upload.wikimedia.org/wikipedia/fr/thumb/0/0a/Bundesliga-logo.svg/1200px-Bundesliga-logo.svg.png",
    "Germany2": "https://upload.wikimedia.org/wikipedia/fr/thumb/1/14/2-Bundesliga-logo.svg/1200px-2-Bundesliga-logo.svg.png",
    "Holland1": "https://upload.wikimedia.org/wikipedia/fr/thumb/3/3e/Eredivisie-Logo.svg/1280px-Eredivisie-Logo.svg.png",
    "Holland2": "https://upload.wikimedia.org/wikipedia/fr/2/27/Keuken_Kampioen_Divisie.jpeg",
    "Italy": "https://store-images.s-microsoft.com/image/apps.57276.13510798886630236.9f5bb184-caf7-40cc-a30c-2d212352958e.2caae805-d616-4564-a457-595caff0a0e2?mode=scale&q=90&h=300&w=300",
    "Poland": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5MYerBm3YWdOgQV1AwguPJxwT82MbjgrKvyqk9Pb3QNv9EIGCQ-9TcJPsI-6Jc_Aukp8&usqp=CAU",
    "Portugal": "https://www.kindpng.com/picc/m/243-2435409_fifa-football-gaming-wiki-liga-nos-logo-2019.png",
    "Scotland": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWPgii9hdJ68_kkOfjVMxH2QYtTzi3qF1l7fhih-gae0OqEBQcIyiBYi941s9Pr0h-ZKo&usqp=CAU",
    "Spain1": "https://www.thesportsdb.com/images/media/league/badge/7onmyv1534768460.png",
    "Spain2": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOUAAADcCAMAAAC4YpZBAAABd1BMVEX///8FE4P7//AAAHwAAHsAAH8AAAAAAHgADIIAEIL+//sAAHUFE4QjK4rx9O79//bs7fXy9Pmhpcnd3uvIzePT1OQACIEAAIJ1mLbx7QDp6en6+/4uR4unFn/tByPznD01OY6GibmQkbzCwteJiYlZpR8/RZZ0dq2tr9EwMoi1uNgwNI+vr69LU6BNTU2UmsEAAGthYWGsssrtAADk5vFwc6tjaad9g7Z7e3tiZqU1NTVHTZkYHYRXXKAVG4JLTpbCwsLd3d2Xl5dAQEAZGRnymC/5zqlOoQB5tUzGy9tWW6N8grI/Qpva3+SOkMAAAGLXo8TjwNfNjrfr0+K3VJb50NL0kJX0bnb4tbn93+PyU1z6vsKtMIfGfrCaAGqxQoz1gooKL4FdbZ7xMD373cL1oqc/WZb1plczTI/1vIX5068AI3n87d70mTaSrcZbhKnz8Feou877+sz19Y/183fj8Nz9/N6jyYjI37pnqjP4+bOLwGy+2a77l/1PAAAZbUlEQVR4nO1dC2PbxpEGvLterABEeDMRkpoPh6TJuFAcgjRNirIdp6llR0kv1/b6vGuv72uTXntp0t79+NtZvBaSCFoiZFKqPj8kUSC4387s7Mzu7EBRLgp75Hl9pz2Zjo/i46jf8Ub2he+1jQhH3iCemQuCECaIkAAByNzsjh3f2nTraoHtTQ5MzElpzDAMlf8R//MvTCMEo+Y4cq+4UO1BvKC4EXBWS2AEBNPhC2/TLb04OjHGRFtKsICGdC0abbq5F4HV72LClguxLFGDIXXshZtu9DlhR0NEWE6CaRyBprEK2oyQg86V4umYVEvoNQjWdYo0Y24O5/wnyn8iRDubLNFnV2eAdhqco8GFg2njYOIMZBtq+wOnHTcJ5Vy5rMtsDRboR/7mGn4OuFPE5agRPJ9Gvn22CoaW78SHDUROW18StK7AxOIskGpoaHHQX2U0bXcQ89F70ghrtLvtamsfUM0g1HRecV4IvZamF2YqQYAnl9vKNdEJCB+N4/MNLS8mOCgNTw2pWzw6I8Kd1J577vdZUROXR2gjcC6hfXUgfEEJOriYECxnSMqjE/dqbl49CMeImoMLv92OMCqJEx1uoYtgd3UUrXWHMC4PT2SeX/cvGZzkbO1GdZolcZLhltmgcKYf1zCZWxMkzyrE3C6a0/1OPTdykKy1DW2b4rG4WVtrXFM2tmS+PTTb47K2jtw1lnOspkwTHWyLpe3Eckvs/thsNIbRhVtnd5FMc1xDC2uAVfI6I5MSjama/uLCN7S7kjQNuhVObSjbnY6K0wjZIBePLMrS1PvrN7JOWLEUR6E1XDR72ChYMrRV84l3T57UA3ONW7ma5L2T+9tigbjmtmgprgiG69xtQKV70a0JUFyTllc3ULzW/SJaGCCNbIkwB2qjxFFlwXqjKYxJ0WtoO4TpoJPLN7i95i0ttbglOaillWuiRUsMDZXp07WVbFDclGlboLLjMklu+0kdKhbnzgFrbJxl2MPy6rHB0LxVy66klftAaFrH/dbCpLyS0SBxXTG+v0hoanjjK7R8TEosNb3ONWO/qxONYLxxH6+FS9F9UHODBr2Xs2jjWwoDaWHc0NBR/UFvuHHDo/iSe85dlIsHldsMW14rJmvEWluNI4kk6l6PpJZTaEtzCB5v3EZcDnxaWB4aX8shySEtz6CtcKcvA8e592rgzXtglwRfyycRdHRNxyQPRHJ91cztWQCvGV4Wyhsq3ao1tlqRb2cY27P2VDvyQN7YbOy3s7sca988bGYbcNp8ozvGu7eWY2fdmxdrMpvV1yqSa7MM72ejkhzV0lp+y+RPOc4K7WVILyuxKuvr+ixzA6vqlfbVaXZzVCxCu8PmvRTDw9zn91vde+YSqJ2TLHcVy3/gFHigrM1ynO1JkWrTc0hQkKJKs9t6oKXIXUV/THAj0PJfyAgClLghu7kUd/ZaQyyBLt7YXZOlZaZuj0YqRemquTvPUIWRKhxiA6fZNG1EKvKk087dKUagN6SldW/NfGNdWfaziGtFglUfF+2q2DmXOsOgwo0KD2hlMni63LWTSVKJaFC+ogaWad8bTK2eRWZF0FK1oeAUnRF0QRXtMVarwJK+yBR2V3mAT6Rl1sDSSne3jBXbWqOgkJH+Sgqroha8EFeTNIKmeN9OylLpnCJZA0snnSwNWr3Q08e51rH5coW19UI5dbCdDq4+upAN3kyUn8yDU9esz3Ka9v2qPeKDQkaktfyyvrRTSfnPI3pKMmWw1OZl+nqITl+zNkubpa1YsatoS3qEK1K7YqkzwHZOyzmkjJVmEcYYaYreTW2P4pxBcn2Wftr3TK+OneWdOVShsKzoDMJtp6+XmkuIOuduwHA4TP0Bw0BJbkyisDu2lLpXnOBYm2WU2oZVW6c9SUYVfqAndQYblUTLobd8d2RZNnf9LAHXdf2kd1NRFtcb2kEu1rVZposEBqpO+bXmksI+WH5dr1A40uWTZ0n/9OWfkYhyt1OInkyLHluXpd1NLJo2r15lHhTTAatYMsluJzqD2862ZGCNqpyhVF/zEBCMkpdTXpela7CVWggYSzI6XH6ZL3UG8pWwK61kM7a8IxPbo7SKTuFd0qmNpZc0g63YVLSahV+JK1K9WwVLbWYrfiBNI1UOk3AJdvzC9Bh4tFMfy34iI7ZijaBTGBGDVFxaaJxKuH5G0rCsXBtMRCm7Tbwr69PYSXLjxjks7OHyKUeWHeyrz6XIompUCtuzIzkUGgl3d+uTZWpi0YqEzkXeXANVOD6RpLBzrrC6pLBVWYaJ6TGD4kMi5VaNLNNAg1bPI15hFYyq9YShpLAxWNiCZBKfnI0d4doVpscIzHCnTpbJUDBI9TzSLsaXtlju+FiSo6P3ldCUFLbS9oAon0vmmD7g5qhGlom5CLrVnro0vkiFbjuSp67bZe+uSgWEgT2Uhv7BTtlFWJOlPRTtrxprSuHrrtLtYrNFDV6WFZZpy9+2A/oqBXYG9uplma75rFiGlWZBhpcPL1vKMIEIRw5HSIWFBZYhKWcjXgJLQ68MoO0i5DOqfCQ5bOFB42guuwSy1xG1C7jKDrCU/F9DH+3eugxZosqoayTN7aTCR4qLzoBVDk9WWHl50NYJyqBbMCp3fMnf5dY58Wpr8wosE/qbBZUXSTIyKrKBrXvFpAqnhKXJk8+e0oXS7M+VE4bgG5LpYQs/XXEf1BWTJLJckXofS/PIveVTjjSpCsdnJg/LmXw/yZEbcJa7csQD6biNBKiuKDrZ7SL3Ky+aobNbewJSZ4ALUPbUJQ/fWrCi9SMFvB6tVNiBpSheW9srgAT16sMirmRFKoxPOJSsZJzHAYl8sDT/dEoKy4el8uKstR4ZtXh4pDIr3ZNW/ytYetKKDe2UVp9VoyENZ2mCoX1Octel1WuZNbGsXr4bSD0dNJc6SZE0rYPDKIUxpajLKpxyhrjC7spezyWxjGGIV7OUl42N0yUWwlFHBJzzssKWsvpUKfNd3m4Zc4VVBrIjaJz57bosj0FQ1QsFrdKoQYeO5/kcnjfoR63pbDin8PaRtKYuXjiQWTIycUOAPZJsGb9uh09ARSBjICpt5xU3qGWtoFqWkxJLg6C8HUhU4AoYDLpI9nVhuhmXNvMMpB4KqNLMiKydW3K8w0jUkdCqbaXSA9+zmmVrhQUUuznhtDhNpIkzYe0Tb2NBEJBAnl64hd3ddSWjdWJN+EFtK5XC2Vw1LqtZiqFqSRcllQ4GZ3ROyZYaQrEl38Gg3IEtUgl26mMZHjZWrYd0VrGEXZN+2VPncBertoGwtbMrrcWD6yBniezWx1K4W9VewWheWTmNaWBi5dAyPcR4tGKCIF1l9w1p2S5Qw1KWSJ0swWqgbuUlLf3MVqZowO77yJSWv9I+82jV2xLLXowGQ+X+0a3LYjmisJZTeQnkBVQ0FtYZOrLiZcFqde+w+UgOQQ0yPZHVVCdLm0uBEZmT50xO1J8KW+Ssen+idiMTW9hjlFsWrZmFLWGsLymvJlgdwHBhUAkSoKnuKZY4/Z0RrL0XPSHcDhSsRocwE85P+Al+bBI+P0JdI02DYIGHDIGox7mY8wjcXvCZM51EdakkQWRiKAQgCRDeBu/DiDpcp0kO2t65VcbOAz37JTbDNfN9IFYtlqzsIQIRBfTkelcIrs7k4P7MFGXwMGEvjybOoOOCY2uLWfxBAnmDwR6MTaQXQCR4eX98zN/X8ULlk+cFvFNZeLtWp/j1urlbIR90xRrecZYxoteYdwh7siN7xeGnk6IsZ97trpvvwx3OIjUtN//sdZ3RzjJgTidU7i7lfAF0kMrUzGLM8vP79DUeIKxMGa2HJVjZPNeniPUaR6/35ExFmnPi8K15f+6Oo+P0eykAqUrQuoJwGcsFJy/KbEX5lvoQI6alCzOFN2Jow+t1bM+nKs4mDmmxFF+zQxfjRl4NRdqO04zrdXLPpyw/Onu/yJ6qpRrDFmGM8q03KWDSKjJEryJcrUghnBXLUtdtZEY4r0vpFlEEI9fr/F54n5jZJmaRjWZsS2W3uuCjfCXPJ9JeQE21HLcFbb2ZCbNVTk66Vpjp2daXnKiz4rzQlcPIzGuCdqh08uWa2VmP5ramSNkw2HUrtdH/NCMklxQJFtdrOlGiRWZr3OJkv0HU6xWcKL18L0HeO21csxhMifM1S2k6MdDsutHM10EO5JSt5jWjGeUbAEcyze0qiLo+cqlZUnSiamjjpc8uCZZcokrDk+sVbeawpFwHg+Hu9Vq7zGHP5O12pLevpzitqUzTwFfosU7nQdgrnfglaLLWnOJuqzK0SrUDDKy1Lxxy2u3tHdnevJTtwajevpg8na0usmcd4VJaAdSUPbdQ7IG57RsvESmJ09BQcL7HBdr9Zt0FTC8BflMvZ8MYhHajV1VAt63uX0IB00tAn52s3K1hfTZY3Xa339T1xcWftPR6YbVUzE48MZCg+czxl9tcy4+6KqZBPaWhXw9GPXYqUVIjmMziyLdOPGowtK1Oe9wk8ITe8fbOH2fC7en4VBYXC+DRkObBpB05A46+E7V6swBRTAKN6PEVjNnsaEjPTFfTCEGYUl3XKadHIN2XU9RaV8LonEbo9YaYBCuyX+GxoGw6uELj8RSsTnwPUtaX5RKyAKH5oXPFhuNZ8PtxwHUTxh4T2ZXwbGGmwROjddw87lxlKZZh+w63M2YA5yIophgFZndyPLgGMjyF0LYta+RyjCx7yaNrb3CDG9zgBhtD/6r6ga8Ob6JTfb2H4G49+l2CjG15xNelQUeNlad5rz4GHlQzXINle90HqtUAp6EaQfWug0XW0Vgf4Yu+tT4MdE1Dq1iyNVhOkHrRt9aHAV35HNS1WI5I8E/A8ohoV4Rl4+Ise1h9PSzdQSvuRZ2TzovtR73YcU+xtDrtOI7kJdxTshx1juP4RCxud2LYgHCdeNLJQ1hrjA2VMe+597wIa3l7xr1+vYG8O4WzlPzfvLxN3ZlBPQPKXmollnZkYooIwtKT7U7I0n6xoHDUEwfTvCtGx11ETcXqEUwwzZKPBkNiGKKUA82rmVoxE2+udQ3Y1xCj2hw3VE2XT2y2KCF43qCQ5yaxtGaU0HkDM5UURz7LsoTHSzca8wZSGUqLlvhTTlkNutY82RdHh8nrrX0dFsGZruv76d183oHE5N4UQysqjp8DFglE4Vn7iKiG9PiWGBvogPd4Z6EZEktbJWQcwilB/rKeZVGXZclJiuMQUFqSJhP+gY5FEQ5MuNTgEGzWQ3bIr9JUO3/egkc1kX7fxnyWpnXlL0cordcNSeAod0L4YEzLHUE5nIJlTNKc4gG/nGTFDkuyhEM7orugXFBaPdP3XFE7iJjOyD6Gt+Y1KlpItj5Ws5Fm876Aqy7+vPIyxiQ9cwKVV/N67fZcM7JqYlNSsPQpWyRqFM4CPpxSYZZkCYUDkwKBXD2CWX5ggEB9AzEeZ0Q6YF5mGWEtrUkAJ/dZdc20V0cLpxV/wsOgyP2OKB9E+QcXLCdI67oJoK5Gdky5JMuBrhq64NBDMBTTl2OSZ9Dz14tqxGWWpkbi5P4+FPSprn/36hiZOhUS8e5pefUuqHqc19mSZhKo1xakp8BFhaiXKcvSuLyv62Jj3gJZ5jLrkbykhYOlZxmUWEJRqeyoOayCV5XzPRds34KMgRkLihplvB+LOlsSS5eb1gAVoGl1q7KNDV3OIHw+XvCA7EyWfWCZGboSSwhuCE5uDl/qPMBuR12KYLsvY+lQ3qXPT7P0qEGOXL9ASuG07zM44o0N1CUsqbpElm2kkrZ0f7++FfC+Rok+dJqFxvIowTiLZYcaZxZ1P+n7eF2dUOQs09jlLFvkkg6mWV1dQzMvsT4pS24PjfwZAjJLXTKO8j3KsuzpBJl9UV7v/CzJeo+bPxtWk7s+4NrZsxLLok9ljcVllzbX2JIsx5hPh6Ki1flZotJjxcPnNWnsQdZ7MkuoYJWrpsTS5+NVOmnk43S2KcmyTw1NFa07P0uoCC4VSuvv12NjocJxMinJLKEUFVtkHnXBcgQlvoonYsc01S5ZlmE3MNIjkpUsz7SxUO1SM/OE9GbFAwnOAyhDlXivocTSFYUE41MsRVFDpj/PmkTO8H2sYtWyalzOz5SlrUIAlHkME0rq8X2AJUlKiS0YsBwJDxTYGOnIFAa3kzMGv2viWpYbEXIv82ODguUIZ1Ui3WYAxiodXGWWmuz7sIBf0RqkHcPfvuiPLMsfk7oskcddDE3t2O4Yska4P2aKw41QHpcZZDIKRzHk95PITlrVJIImaTYhYMuGopBl5u1BUgaNbKsNueRs7vf2hdjAYTZzlkXNXbABaBC2daFHLg+pIUdw3mwSwmhNoVcIjpSGGjy0hfZrCCclLCbiADni4Zcodmc0WBJmuUmmLdM0zisvUwKdkhcSEKU6UUB4ICxSpggGpbX5dMyCpNVjHjpLxgriV4bSWMxJDjQxqNR6qkLRhdGGx+wwpuntIxAaGqZKOBYnGw3GyJwZRoBRmtnkaenZDYayQrR89ofn6qD5VHREUi6BMToVZ5MCGPb+dEH4JRo6ivzpEL5leJYsTYQIatgwnJl0R0/LQWr1keTjhSJYFBhw5YVljnzOd0z4BdWcgY7QoZO/7o4xhgpTQS8/UU9JAIWuSNqsPtcL/rfFnXtEqCmeIpVe0sCHTlKkiss6taWdBsTWcW5nOl34AETNWp0gr9c9cGDUdWZHA2kWtgbT7pHjKqPuiTxav33E31EMGdvNkF7mHs9mx77okW6UPNstv8RSpG/TyyfdsXx22/Yms+74SmdT3eAGN7jBDW5wgxvc4FrC+ux7m27CpSP8l3d+/rNNN+Ky8fk7HP8afv8HP/zhD/7tR5tuzSXhe+8IWL/+APCtH/9k0w26DHyekHzn8x998C2BD358/eRp/zRl+TPlWyk++P6mG1U7Pvt5SvJz5YeJMD+4Ziprv3iu2J/9O5CEiQQGJif5H5tuVs3o/OIXv3yuhJ/9VJBUfvSTn/zgPz/4sfKr72QX7L3/7cfwNXz4PuBh+J74+vRKHeNpv/3227/4pavYkkvwa3v3zkcZzb3bt9+Dr+G3bwMehXfF19vvb6CxF8Zv3gaaYpMlfPzee0/Eizu//dOdj36VXCCxfBjCSay7t7+9Fz69ffvphlpcCff5mS//Dlj+BhYgnzx5/Ojuk8ewBPv7j+7c+dOd5AKZpXjhrhDj+7c/fA2NPi9C8+wM7bcFSxtI8n/8Ok7pV5zknTsf/UFcsITlw9uPKj4s/yZP/1Kqx/HS35bef/qqE6/YnbNvJ2T5u5GigI15zH/74WOhsFyYvxUXnM3y8e3bd5e0yz7QUXLCQ6eENET97tFMR/sxfHYTdt6cffjv0wE84gq2MvZRQ1eTLRl/X36A24FOqC6qPHn7tmJRuK37KafShj2scLqPkjTFptiHG2CKTfg461P4eVHsA4hx+V8dZe/Z072ntx9xreVc/pgIc+cES8CHmfV5treEZXtohR60REF9PpBhBFj3jqxwtIA8wCPYNe8j+I/OR4oFneAjL7SjfbEd25tTaf3+/iS0fZE/6EH6n+AWwQZgBBvu7Tn/JJEQedgTN3RCa7I/gm1uSJdqFvvnDrc9v3lgK0+4KJ8BoT3g9HsQZmJ/JJbPPnz06H1g+ejRhw+XkVRi6EcHmpxnJzk6cPWdsMTSbI6VUcoSWgpZV/ZiMJM29A9BUn0oAilYuvv8ahWGnmAZw75jv5OxFPVUwu4LYDkzbZmlLzhyMnsw1kBAnK7yh48AfzjB8qG9xy8DG7tXsR3t6912Qq8xbbdaoDbxDDZaRKKQxHLm045VsGzDnuSgydkXo0qw9OHhoIIl9IS/b2UsfdRMtpEFy1GSddBuhoq1P+I6LLEMH4SKaDK3PI/3uAnag8nkj98B/PEkS/GOuyunykHLFI9BIOMoiuCjxrzT/cMu7AzfFyzhFEf/nhLtu4uCJWwjvpxPpvtF3sJJlgPV7ondxqibftI9kUMJLN3koRPREFja/qdeVy4j88kXX34CLD+EqeG9Z0/hARF8RGZPgTgvy/A57+twDGqba2xE4f8R4po3hkZGDWDZDMPusOFmLGcTMEZRfzArcrQES2duZSxD3DYHOUvI+Ql745SlshCzyAH/ZIvL+1g1cpbhJ1+8ySFoPnpi74Hn9re3AH8uWD7lirr3yiy705BbPxgjWFgfeJQVbvHXjoGlwweZfQg8+vdCxdWJYNkJRxOQ9DE0vlPkPR9y6zMQScsJS6VHmZKznHEdD4UZECzbUEGxD0YMWIZzPWdpffmmwH9Dtzx5ApOm8peTLJ89evTsofKqGuvr89gURcgRRhiLvBlPN8dzAo9RsoYoNkVqggPjrwUK51JM9K4Pz4wGyxOqee3SKcU0qcHvCQPGb55sOrchlcAnLL5H4ZO6QDXs7U+7IhXS+hSkX7BUvkhYvvlF0cy/Cpb/k7F8BHh2V3n/WTJDPn32sJIlv//gdAat18kE5J/x24vixL3swZISUGHKMvH/vuKjMVHYt/5SW1O2AbYg+aW989VXX3398dfKrYTkW7c23bB6YQulVb75+N2P+d9vdv4sSP51082qHc/f/PIL5euP3xV4Y1ew3N10oy4Bo0+U7yYkP/77G3+7dqMyx62/pyzf/Ub5x1v/2HRzLgnffJxw/Por/sM1lSRn+V2O//2/r87xlv8H1LaN1QLSO0cAAAAASUVORK5CYII=",
    "Sweden": "https://pbs.twimg.com/profile_images/1111583953910198273/hmyjzwP5_400x400.jpg",
    "Turkey": "https://upload.wikimedia.org/wikipedia/fr/thumb/4/4c/Logo_de_la_Spor_Toto_S%C3%BCper_Lig_%282010%29.svg/1200px-Logo_de_la_Spor_Toto_S%C3%BCper_Lig_%282010%29.svg.png",
    "USA": "https://cdn.worldvectorlogo.com/logos/major-league-soccer.svg"
}