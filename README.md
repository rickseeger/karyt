
# Karyt

Karyt (pronounced "carrot") is a service that allows people to
associate a bitcoin address with an email address. The bitcoin address
can then be retrieved with a simple HTTP request. For example:

    http://kar.yt/john.doe@example.com

returns:

    15tqoVno7i3qH7TMcCpN1JrHDZTm2nHVow

in the body of an HTTP response. Bitcoin wallets can be configured to
support sending bitcoin to an email address by retrieving the bitcoin
address from the Karyt server in the background.
