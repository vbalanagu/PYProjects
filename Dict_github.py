import requests
url = f"https://api.github.com/repos/kubernetes/kubernetes/pulls"
response = requests.get(url)
status_code = response.status_code
if status_code == 200 :
    output = response.json()
    pr_creator = {}
    for pull in output:
        creator = pull['user']['login']
        if creator in pr_creator:
            pr_creator[creator] += 1
        else:
            pr_creator[creator] = 1
    print("Printing Creators and counts")
    for creator, count in pr_creator.items():
        print(f"{creator}: {count} PR(s)")
else:
    print(f"Unable to do the pull request and response code is {status_code}")