# Runs the ./runtest utility and parses the output into json.

import os
import json

languages = ['ruby', 'shell', 'c', 'mysql']
results = {}
passed = 0
total = 20
for language in languages:
    output = ""
    try:
        p = os.popen("/grading/runtest {}".format(language))
        output = p.read()
        score = output.split("Passed")[1].split(" out of ")[0]
        max_score = output.split("Passed")[1].split(" out of ")[1].split(" tests")[0]
        passed += int(score)
        p.close()
        results[language] = {'status': "ran",
                             'score': score,
                             'max_score': max_score}
    except Exception as e:
        results[language] = {'status': "failed",
                             'message': output}

print(json.dumps({'results': results, 'score': passed, 'total': total}))
