import click
import requests
from subprocess import check_call


@click.command
@click.option("--dockerfile", type=click.Path(exists=True), default="Dockerfile")
@click.option("--path", type=click.Path(), default=".")
@click.option("--registry", type=str, default="docker.coyle.club")
@click.option("--branch", type=str)
@click.option("--default-branch", type=str, default="main")
@click.argument("name")
def main(dockerfile, path, registry, branch, default_branch, name):
    if branch != default_branch:
        name = f"{name}/branch"
    resp = requests.post(
        f"https://tickets.default.svc.coyle.club/pool/docker-images",
        params={"pool": name},
    )
    resp.raise_for_status()
    number = resp.json()["start"]
    tag = f"{name}:{number}"
    check_call(["buildah", "bud", "-f", dockerfile, "-t", tag, path])
    check_call(["buildah", "push", tag, f"docker://{registry}/{tag}"])
    print("Docker image:")
    print(f"{registry}/{tag}")


if __name__ == "__main__":
    main()
