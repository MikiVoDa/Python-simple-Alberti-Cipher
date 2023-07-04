
def rotate(input, n):
    return input[n:] + input[:n]


def decipher(ciphredText):

    largeWheel = "ABCDEFGILMNOPQRSTVXZ1234"
    smallWheel = "gklnprtuz&xysomqihfdbace"
    cipherIndex = ""

    ciphredText_arr = list(ciphredText)
    i = 0
    first_char = ciphredText_arr[0]
    decipher = ""
    endIndex = len(ciphredText_arr) - 1

    if first_char > 'A' and first_char < 'Z':
        ind = largeWheel.index(first_char)
        cipherIndex = smallWheel[ind]
        i += 1


    while i <= endIndex:
        crt_char = ciphredText_arr[i]
        foundUpperCase = False

        if crt_char > 'A' and crt_char < 'Z':
            indexLargeWheel = largeWheel.index(crt_char)
            indexSmallWheel = smallWheel.index(cipherIndex)
            q = indexLargeWheel - indexSmallWheel

            if q < 0:
                largeWheel = rotate(largeWheel, -q)
            if q > 0:
                largeWheel = rotate(largeWheel, q)

            foundUpperCase = True

        if foundUpperCase == False:
            indexToSearch = smallWheel.index(crt_char)
            correspLetter = largeWheel[indexToSearch]
            decipher += correspLetter

        i += 1

    if decipher == "":
        decipher = "N/A"

    return decipher

# Driver Code

ciphredText = "BgxggmpDxlsl"
print(decipher(ciphredText))

ciphredText = "Bgxggmp&pmp"
print(decipher(ciphredText))

ciphredText = "BgxggmpDxlslBquih"
print(decipher(ciphredText))

ciphredText = "CkEkBk"
print(decipher(ciphredText))