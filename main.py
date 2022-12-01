import helpers as gh

if __name__ == "__main__":
    lst_repos = gh.get_repos_from_team()
    count_errors = 0
    count_repos = 0
    for repo in lst_repos:
        # filter repos with subfixes: -interactor, -business, -presenter
        if "-interactor" in repo.name or "-business" in repo.name or "-presenter" in repo.name:
            count_repos += 1
            pulls = gh.get_pulls_opened(repo)

            if gh.has_pulls_release_candidates(pulls):
                print(
                    f"❌ {repo.name} has release-candidate pulls ({repo.html_url}/pulls)")
                count_errors += 1
            elif gh.has_opened_pull_request(pulls):
                print(f"⚠️ {repo.name} has opened PR's ({repo.html_url}/pulls)")
                count_errors += 1

            if not gh.compare_status(repo):
                print(
                    f"❌ {repo.name} master is different to release ({repo.html_url})")
                count_errors += 1

    print(f"\nRepos filtered -> {count_repos} from {len(lst_repos)}")

    if count_errors > 0:
        print(f"Please check before to deploy, num erros -> {count_errors}")
    else:
        print("🚀 Ready to deploy")
