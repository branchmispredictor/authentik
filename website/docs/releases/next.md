---
title: Release 2022.1
slug: "2022.1"
---

## Breaking changes

This release mostly removes legacy fields and features that have been deprecated for several releases.

- LDAP Outposts:

  This release removes the `accountStatus` and `superuser` fields. Use the direct replacements `goauthentik.io/ldap/active` and `goauthentik.io/ldap/superuser`.

- Proxy Outposts:

  This release consolidates headers sent by authentik to have a common prefix.

  The following headers have been removed:

	- X-Auth-Username, use `X-authentik-username`
	- X-Auth-Groups, use `X-authentik-groups`
	- X-Forwarded-Email, use `X-authentik-email`
	- X-Forwarded-Preferred-Username, use `X-authentik-username`
	- X-Forwarded-User, use `X-authentik-uid`

- API:

  The deprecated /api/v2beta/ Endpoint is removed. Use `/api/v3/`.

## Minor changes/fixes

- core: dont return 404 when trying to view key of expired token
- crypto: fully parse certificate on validation in serializer to prevent invalid certificates from being saved
- flows: handle error if flow title contains invalid format string
- providers/oauth2: change default redirect uri behaviour; set first used url when blank and use star for wildcard
- root: decrease to 10 backup history
- root: fix backups running every minute instead of once
- stages/authenticator_webauthn: make more WebAuthn options configurable
- web: add polyfill for Intl.ListFormat
- web: directly read csrf token before injecting into request
- web: fix double plural in label
- web/admin: fix missing configure flow setting on webuahtn setup stage form
- web/flows: remove node directly instead of using removeChild()

## Upgrading

This release does not introduce any new requirements.

### docker-compose

Download the docker-compose file for 2022.1 from [here](https://goauthentik.io/version/2022.1/docker-compose.yml). Afterwards, simply run `docker-compose up -d`.

### Kubernetes

Update your values to use the new images:

```yaml
image:
  repository: ghcr.io/goauthentik/server
  tag: 2022.1.1-rc1
```
