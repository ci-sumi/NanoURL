# NanoURL

![Flask Image](flask.jpg)

A URL shortener written in Python.

## Developers

- Her Majesty Sumi [GitHub](https://github.com/ci-sumi) / [Linkedin](https://www.linkedin.com/in/sumi-tharayil-surendran-33ba69268/)
- Tomislav Dukez: [GitHub](https://github.com/tomdu3) / [Linkedin](https://www.linkedin.com/in/tomislav-dukez)

## Tech

- [UV](https://astral.sh/uv/) - A Rust based Python package and project management tool.
- [Flask](https://flask.palletsprojects.com/en/2.2.x/) - A lightweight web framework based on Python and used to build web applications and APIs.
- [PyShorteners](https://github.com/ellisonleao/pyshorteners) - Python library that bridges to various third party shortening services like TinyUrl,Bitly etc..

## Local Deployment

- **Windows**

1. Installation

```sh
irm https://astral.sh/uv/install.ps1 | iex
git clone https://github.com/ci-sumi/NanoURL.git
cd NanoURL
uv sync
# activate virtual environment
.venv\Scripts\activate
```

1. Run script

```sh
uv run main.py
```

Git tips from Tomi
```sh
git remote show origin
[-Scenario- git pull was pulling from origin/master
git push was pushing to origin/main]
git branch -u origin/main main

```

## Vercel Deployment

1. **Prerequisites**
   - A Vercel Account.
   - An external PostgreSQL database (e.g., Supabase, Neon, or Vercel Postgres).
   - A configuration file `vercel.json` in the root (already exists).
   - A `requirements.txt` file (already exists).

2. **Setup Environment Variables on Vercel**
   Add the following environment variables in your Vercel Project Settings:
   - `DATABASE_URL`: Your production PostgreSQL connection string.
   - `HASHIDS_SALT`: A secret key/salt for encoding short URLs.

3. **Deploy using Vercel CLI**
   Install the Vercel CLI and run the deploy command:
   ```sh
   # Install Vercel CLI globally
   npm install -g vercel

   # Login to your Vercel account
   vercel login

   # Deploy the project
   vercel
   ```
   Follow the prompts to link and deploy your application.

4. **Deploy via GitHub (Recommended)**
   - Push your code to a GitHub repository.
   - Import the repository in your Vercel Dashboard.
   - Configure the environment variables in the settings and click **Deploy**. Vercel will automatically redeploy on every commit to `main`.

## References

- [Title 1](https://medium.com/@dieggo.filipe/uv-the-new-python-package-manager-you-need-to-know-492a147af74c)
- [Video 1](https://www.youtube.com/watch?v=AMdG7IjgSPM)
- [Video 2](https://youtu.be/5rTwOt9Qgik)
- [Flask Video](https://www.youtube.com/watch?v=mqhxxeeTbu0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX)
- [Flask Video 2](https://www.youtube.com/watch?v=45P3xQPaYxc)

I came across a Git issue in our main project NanoURL
![image](https://hackmd.io/_uploads/r1TWp8Q0Zx.png)

it solved after running this command
```sh
rm -f .git/index.lock
```

Issue : Git created a teporary lock file(A git process was interupted or git didn't cleanu properly)

Antigravity
Deployment
Scrambled data or piece of information beyond recognition.
They are designed to be irreversible .
To reduce the collion salting can be applied.(Random data can be added before hashing)




