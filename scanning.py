Remove null bytes
Find/Replace (\x00) -> (\u0000)
Find/Replace (\\x00) -> ()
Find/Replace (\\u0000) -> ()
From Base64
URL Decode
Find/Replace (\\) -> ()
JavaScript Beautify
Unescape Unicode Characters
Find/Replace (-encodedCommand ([A-Za-z0-9+/=]+)) -> ($1)
From Base64