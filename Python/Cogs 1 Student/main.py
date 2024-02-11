import bardapi
from bardapi import BardCookies

cookie_dict = {
"_Secure_1PSID" : "fgg6G_OX5O_Yqt2k76RzJ9eEQxndBTbz3EFz912pFTCQPUmNAjOtDTBBptow3CRGnoM2Dg.",
"_Secure_1PSIDTS" : "sidts-CjIBPVxjSvm1MgkHzz1kAmUCyo0Oo-AadKCuHLt8sVII_EU5y1jmGMIcgnpEoNUFcKFnNBAA",
"_Secure_1PSIDCC" : "ABTWhQFGMJ3YCZQGUTdodIcX9wdXogVqD99eK_Hgxf1s1ziCka6g1yfO4zl8Yuj_yEZ9Lbg3I1ig"
}

bard = BardCookies(cookie_dict=cookie_dict)

print(bard.get_answer("Explain about peptide compounds and structures")['content'])