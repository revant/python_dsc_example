import io

from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from pyhanko.sign import signers

# pfx_file will come from S3 instead of keys/secret.pfx generated manually
# passphrase should be saved along with file id in an entity
# convert passphrase to bytes

signer = signers.SimpleSigner.load_pkcs12(
    pfx_file="keys/secret.pfx", passphrase=b"12345678"
)

with open("document.pdf", "rb") as doc:
    w = IncrementalPdfFileWriter(doc)
    out = signers.sign_pdf(
        w,
        signers.PdfSignatureMetadata(field_name="Signature1"),
        signer=signer,
    )
    with open("signed.pdf", "wb") as f:
        f.write(out.getbuffer())
