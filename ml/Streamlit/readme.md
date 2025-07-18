## 📌 Animation URLs Table

| *Category*       | *Animation*            | *JSON URL* |
|--------------------|--------------------------|-------------|
| Loading           | Loading Spinner          | [Link](https://assets9.lottiefiles.com/packages/lf20_usmfx6bp.json) |
| Loading           | Loading Dots             | [Link](https://assets2.lottiefiles.com/packages/lf20_hdy0htc0.json) |
| Loading           | Loading Bar              | [Link](https://assets8.lottiefiles.com/packages/lf20_vfdkv6om.json) |
| Loading           | Circular Loader          | [Link](https://assets1.lottiefiles.com/packages/lf20_q5pk6p1k.json) |
| Loading           | Simple Loader            | [Link](https://assets10.lottiefiles.com/packages/lf20_bhw1ul4g.json) |
| Success           | Success Checkmark        | [Link](https://assets2.lottiefiles.com/packages/lf20_touohxv0.json) |
| Success           | Success + Confetti       | [Link](https://assets4.lottiefiles.com/packages/lf20_jbrw3hcz.json) |
| Success           | Done ✔ Animation         | [Link](https://assets7.lottiefiles.com/packages/lf20_jzq2az8g.json) |
| Error / Warning   | Error Cross              | [Link](https://assets2.lottiefiles.com/packages/lf20_qp1q7mct.json) |
| Error / Warning   | Alert Animation          | [Link](https://assets9.lottiefiles.com/packages/lf20_jz6g8znp.json) |
| Error / Warning   | Warning Sign             | [Link](https://assets8.lottiefiles.com/packages/lf20_kyu7xb1v.json) |
| AI / ML           | Data Analysis            | [Link](https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json) |
| AI / ML           | AI Brain                 | [Link](https://assets3.lottiefiles.com/packages/lf20_bdlrkrqv.json) |
| AI / ML           | Machine Learning Model   | [Link](https://assets10.lottiefiles.com/packages/lf20_dyqfnxau.json) |
| AI / ML           | Neural Network           | [Link](https://assets6.lottiefiles.com/packages/lf20_o7wz8d5x.json) |
| Coding / Tech     | Coding Animation         | [Link](https://assets1.lottiefiles.com/packages/lf20_gjmecwii.json) |
| Coding / Tech     | Programmer Working       | [Link](https://assets8.lottiefiles.com/packages/lf20_x62chJ.json) |
| Coding / Tech     | Developer Desk           | [Link](https://assets2.lottiefiles.com/packages/lf20_gigyrcoy.json) |
| Coding / Tech     | API Integration          | [Link](https://assets9.lottiefiles.com/packages/lf20_2ks7jvhv.json) |
| Coding / Tech     | Cloud Deployment         | [Link](https://assets3.lottiefiles.com/packages/lf20_zrqthn6o.json) |
| Fun / UI          | Party Confetti           | [Link](https://assets9.lottiefiles.com/packages/lf20_q5pk6p1k.json) |
| Fun / UI          | Heart Like               | [Link](https://assets10.lottiefiles.com/packages/lf20_xlkxtmul.json) |
| Fun / UI          | Fireworks                | [Link](https://assets4.lottiefiles.com/packages/lf20_vfdkv6om.json) |
| Fun / UI          | Celebration              | [Link](https://assets6.lottiefiles.com/packages/lf20_fyye8szy.json) |
| Fun / UI          | Emoji Reaction           | [Link](https://assets7.lottiefiles.com/packages/lf20_vgttfyaz.json) |
| Data Viz          | Bar Chart Animation      | [Link](https://assets10.lottiefiles.com/packages/lf20_7pvyv9sk.json) |
| Data Viz          | Pie Chart Animation      | [Link](https://assets2.lottiefiles.com/packages/lf20_t0cjqj.json) |
| Data Viz          | Line Graph Animation     | [Link](https://assets8.lottiefiles.com/packages/lf20_zrqthn6o.json) |
| Data Viz          | Dashboard Analytics      | [Link](https://assets1.lottiefiles.com/packages/lf20_ye3fehx0.json) |

## Animation
```python
from streamlit_lottie import st_lottie
import requests

def load(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()
lott=load("https://assets1.lottiefiles.com/packages/lf20_gjmecwii.json")
st_lottie(lott,height=300)
```
