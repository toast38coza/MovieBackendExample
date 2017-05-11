## MovieBackend

> A Proof of concept, using DRF to proxy a known data-model to/from various different service backends

### How it workds:

It's all in the `api` package.

1. `api.api` -> traditional DRF ViewSets
2. `api.mixins.BackendMixin` -> A mixins to be used in conjunction with `viewsets.ModelViewSet`. It fetches data from upstream services and turns it into `Movie` models
3. `api.backends.apibackend` -> backend factory
4. `api.backends.omdb.OMDBBackend` -> an example backend for OMDB

### Example:

![Example flow](https://s3.amazonaws.com/dropbox.christo/sequence-diagram.png)
