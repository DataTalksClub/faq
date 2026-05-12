---
id: 55c1151596
question: 'eb local run: ''NotSupportedError - You can use eb local only with preconfigured, generic and multicontainer Docker platforms'''
sort_order: 70
---

Recent EB CLI versions don't support `eb local` for the default Docker platform. Three workarounds:

- Re-init with `eb init -i` and pick the default Docker platform option, or edit `.elasticbeanstalk/config.yml` to set `default_platform: Docker running on 64bit Amazon Linux 2023`.
- Downgrade the CLI: `pipenv install awsebcli==3.19.4 --dev`.
- Skip `eb local` entirely — `docker build` and `docker run` locally do the same job.
