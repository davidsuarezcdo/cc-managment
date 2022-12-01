from decouple import config
from github import Github
from typing import List
from github.Repository import Repository
from github.PullRequest import PullRequest

GITHUB_TOKEN: str = config("GITHUB_TOKEN")  # type: ignore
GITHUB_ORG: str = config("GITHUB_ORG")  # type: ignore
GITHUB_TEAM_SLUG: str = config("GITHUB_TEAM_SLUG")  # type: ignore

github_client: Github = Github(GITHUB_TOKEN)


def get_repos_from_team() -> List[Repository]:
    org = github_client.get_organization(GITHUB_ORG)
    team = org.get_team_by_slug(GITHUB_TEAM_SLUG)

    current_page = 0
    lst_repos = []
    browser = team.get_repos()
    repos = browser.get_page(current_page)

    while repos:
        lst_repos.extend(repos)
        current_page += 1
        repos = browser.get_page(current_page)

    return lst_repos


def get_pulls_opened(repo: Repository) -> List[PullRequest]:
    lst_pulls = []
    try:
        browser = repo.get_pulls(state="open")
        current_page = 0
        pulls = browser.get_page(current_page)
        while pulls:
            lst_pulls.extend(pulls)
            current_page += 1
            pulls = browser.get_page(current_page)
    except:
        pass
    return lst_pulls


def has_opened_pull_request(pulls: List[PullRequest]) -> bool:
    return len(pulls) > 0


def has_pulls_release_candidates(pulls: List[PullRequest]) -> bool:
    for pull in pulls:
        if "release-candidate" in pull.head.ref:
            return True
    return False


def compare_status(repo: Repository) -> bool:
    try:
        compare = repo.compare("master", "release")
        return compare.status == "identical"
    except:
        return False
