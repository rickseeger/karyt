
# kar.yt

kar.yt (pronounced "carrot") is an API written in Go that allows people create permanent labels for Bitcoin addresses. For example:

    http://kar.yt/JoeSmith

might redirect to:

     bitcoin:1A4zo4iSuxL4LBNCnjRexTwFvs7jZbGCia

which will attempt to launch an external application to handle the bitcoin protocol.


## API V1

### /v1/create

Create a new alias. Required parameters: alias, address

    http://kar.yt/v1/create?alias=JoeSmith&address=1A4zo4iSuxL4LBNCnjRexTwFvs7jZbGCia

The alias must consist of alphanumeric characters only, and the Bitcoin address must be valid (the checksum is verified).

Possible responses:

- success
- missing argument 'alias'
- missing argument 'address'
- name contains non-alphanumeric characters
- invalid Bitcoin address
- rate limited 

