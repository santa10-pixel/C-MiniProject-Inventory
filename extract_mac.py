import sys
import Quartz
import Vision
from Foundation import NSURL

def extract_text(image_path):
    url = NSURL.fileURLWithPath_(image_path)
    request = Vision.VNRecognizeTextRequest.alloc().init()
    handler = Vision.VNImageRequestHandler.alloc().initWithURL_options_(url, None)
    
    success, error = handler.performRequests_error_([request], None)
    if not success:
        return f"Error: {error}"
    
    out = []
    for observation in request.results():
        out.append(observation.topCandidates_(1)[0].string())
    return "\n".join(out)

for path in sys.argv[1:]:
    print(f"--- {path} ---")
    print(extract_text(path))
