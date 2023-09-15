import requests
import json
VERSION = "v1.0.6"

class gh:
    TOKEN="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"
    OWNER="jtw5734"
    REPO="simple-python-pyinstaller-app"
    TAG = "v1.0.0"
    RELEASE_ID=""
    
    header = {"Accept" : "application/vnd.github+json", "Authorization" : f"Bearer {TOKEN}", "X-GitHub-Api-Version" : "2022-11-28"}


    def get_releases(self):
        print(self.header)
        res = requests.get(f"https://api.github.com/repos/{self.OWNER}/{self.REPO}/releases/latest", headers= self.header)

        if (res.status_code) == 200:
            # print(json.dumps(res.json(), ensure_ascii=False, indent=3))
            res = res.json()
            self.RELEASE_ID = res.get("id")
        else :
            print("error")
        
    def update_version(self):
        data = {
            "self.TAG_name":VERSION,
            "target_commitish":"master",
            "name":VERSION,
            "body":"Description of the release",
            "draft":False
        }
        res = requests.patch(f"https://api.github.com/repos/{self.OWNER}/{self.REPO}/releases/{self.RELEASE_ID}", headers= self.header, data=json.dumps(data))
        if (res.status_code) == 200:
            print(json.dumps(res.json(), ensure_ascii=False, indent=3))
            res = res.json()
            for asset in res.get("assets") :
                self.asset_id = asset.get("id")
                self.update_assats()
                break
        else :
            print("error")
        
    def update_assats(self):
        data = {"name":f"dist/dot_local_api",
                "label":f"dot_local_api_{VERSION}"}
        res = requests.patch(f"  https://api.github.com/repos/{self.OWNER}/{self.REPO}/releases/assets/{self.asset_id}", headers= self.header, data=json.dumps(data))
        print(json.dumps(res.json(), ensure_ascii=False, indent=3))

if __name__ == "__main__":
    g = gh()
    g.get_releases()
    g.update_version()