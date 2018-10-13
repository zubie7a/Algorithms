# https://app.codesignal.com/company-challenges/dropbox/RMJDiTprBf5HQY3oa
def campusCup(emails):
    # For CampusCup, when somebody registers, the institution receives 20
    # points. When it has 100 points, all the registered members get 3GB.
    # When it reaches 200, an extra 8GB. Then at 300, everyone gets 15GB.
    # Finally at 500, the members get a final extra 25GB. So in the end
    # everyone gets at most 51GB. Create a scoreboard of schools and the
    # amount of bonus space they have received (per student, not total).
    universities = {}
    for email in emails:
        domain = email.split("@")[-1]
        if domain in universities:
            universities[domain] += 1
        else:
            universities[domain] = 1

    # Function to get the amount of bonus GB each student receives
    # based on the amount of students registered for a same domain.
    def get_space(registered):
        space = 0
        if (registered >= 5):
            space += 3
        if (registered >= 10):
            space += 8
        if (registered >= 15):
            space += 15
        if (registered >= 25):
            space += 25
        return space

    scoreboard = []
    for domain, registered in universities.items():
        # Revert the map from universities to number of students registered
        # to a list of tuples from score to the university domain, so we can
        # sort the list primarily on space while keeping the domain.
        scoreboard.append((get_space(registered), domain))

    # The space is compared as negative to be able to sort the space from
    # highest to lowest, but maintain the alphabet ordering of domains.
    # Python2 allowed a `cmp` function but Python3 only allows a `key`.
    def key_score(score):
        return (-score[0], score[1])

    # Once it's sorted, don't return the space per student, only the domain.
    return list(map(lambda x: x[1], sorted(scoreboard, key=key_score)))
