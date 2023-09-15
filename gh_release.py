import requests
import json
import os
VERSION = "v1.0.7"

class gh:
    # TOKEN="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"
    OWNER="jtw5734"
    REPO="simple-python-pyinstaller-app"
    
    header = {"Accept" : "application/vnd.github+json", "Authorization" : f"Bearer {TOKEN}", "X-GitHub-Api-Version" : "2022-11-28"}


    def get_releases(self):
        res = requests.get(f"https://api.github.com/repos/{self.OWNER}/{self.REPO}/releases/latest", headers= self.header)

        print(json.dumps(res.json(), ensure_ascii=False, indent=3))
        if (res.status_code) == 200:
            res = res.json()
            self.RELEASE_ID = res.get("id")
            return True
        else :
            print("error")
        return False
        
    def update_version(self):
        if self.get_releases() :
            data = {
                "self.TAG_name":VERSION,
                "target_commitish":"master",
                "name":VERSION,
                "body":"Description of the release",
                "draft":False
            }
            # print(self.RELEASE_ID)
            res = requests.patch(f"https://api.github.com/repos/{self.OWNER}/{self.REPO}/releases/{self.RELEASE_ID}", headers= self.header, data=json.dumps(data))
            # print(json.dumps(res.json(), ensure_ascii=False, indent=3))
            if (res.status_code) == 200:
                res = res.json()
                for asset in res.get("assets") :
                    self.asset_id = asset.get("id")
                    self.update_assats()
                    break
            else :
                print("update release version fail ")
        else :
            print("release info get error")
        
    def update_assats(self):
        if ( os.path.isfile("dist/dot_local_api") ==False ):
            print('upload file is Nothing')
            return
        data = {"name":f"dist/dot_local_api",
                "label":f"dot_local_api_{VERSION}"}
        res = requests.patch(f"  https://api.github.com/repos/{self.OWNER}/{self.REPO}/releases/assets/{self.asset_id}", headers= self.header, data=json.dumps(data))
        print(json.dumps(res.json(), ensure_ascii=False, indent=3))

if __name__ == "__main__":
    g = gh()
    # g.get_releases()
    g.update_version()