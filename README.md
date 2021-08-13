Version
-------
v1.0.0 - 12th August 2021

Application Url: http://ec2-63-33-220-22.eu-west-1.compute.amazonaws.com

Introduction
------------
This project is developed to explore the basic features of AWS Codestar as a AWS Native CICD pipeline service that can replicate some CI functionality depending on your configure (e.g. Managed service like AWS Elastic Beanstalk V unmanaged service like EC2 straight) and CD functionality to AWS endpoint service products like ECS, EC2, AKS, plus more.

Danjo was used with AWS EBS as a managed (server) service. The focus will be on CICD updates, and below will feature a small write up about the observations from updates from v1.0.0 to v1.0.1 and so on. The Python/Django application is a simple static application for simplicity sake; so not to draw focus from the infrastructure aspects of this project, which is essentially the exploration of Codestar as a CICD platform for AWS hosted applications. 

Overview
--------
Python was chosen with Danjo for the simple reason that its the most difficult to implement in my view as its not as developed as general purpose languages like Java/SpringBoot or C#/ASP.NET that have had major backing for allot longer, thus making the AWS offering on Python Django all the more attractive to explore in this exploratory CodeStar project. Also, I think Python is awsome!!

Pipeline
--------
-> Github Public Repo 
--> via AWS Github Repo Conn 
---> AWS (Codestar) CodeBuild 
----> AWS (Codestar) CloudFormation
-----> AWS (Codestar) CloudFormation to Elastic Beanstalk Managed EC2 Instance

Cost
-----
Interestingly, Codestar, Elastic Beanstalk, Cloudformation and AWS Certificate Manager (For Public SSL Certs only) do not add to cost as the cost is incurred in the resources they manage (docs checked Aug 10th 2021), which is of interest given Jenkins deploying to CodeDeploy is seen as popular choice for CICD deployments based on cost alone. A sister project to compare costs maybe forthcoming to see if the proof is in the pudding so to speak.

Observation Write Up - Updates
------------------------------
Pending


AWS README.Md for those Interested is as below:
-----------------------------------------------

Welcome to the AWS CodeStar sample web application
==================================================

This sample code helps get you started with a simple Django web application
deployed by AWS Elastic Beanstalk and AWS CloudFormation.

What's Here
-----------

This sample includes:

* README.md - this file
* ebdjango/ - this directory contains your Django project files. Note that this
  directory contains a Django config file (settings.py) that includes a pre-defined
  SECRET_KEY. Before running in a production environment, you should replace this
  application key with one you generate
  (see https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/#secret-key for details)
* helloworld/ - this directory contains your Django application files
* manage.py - this Python script is used to start your Django web application
* .ebextensions/ - this directory contains the Django configuration file that
  allows AWS Elastic Beanstalk to deploy your Django application
* buildspec.yml - this file is used by AWS CodeBuild to build and test
  your application
* requirements.txt - this file is used to install Python dependencies needed by
  the Django application
* template.yml - this file contains the description of AWS resources used by AWS
  CloudFormation to deploy your infrastructure
* template-configuration.json - this file contains the project ARN with placeholders used for tagging resources with the project ID

Getting Started
---------------

These directions assume you want to develop on your local computer, and not
from the Amazon EC2 instance itself. If you're on the Amazon EC2 instance, the
virtual environment is already set up for you, and you can start working on the
code.

To work on the sample code, you'll need to clone your project's repository to your
local computer. If you haven't, do that first. You can find instructions in the AWS CodeStar user guide at https://docs.aws.amazon.com/codestar/latest/userguide/getting-started.html#clone-repo.

1. Create a Python virtual environment for your Django project. This virtual
   environment allows you to isolate this project and install any packages you
   need without affecting the system Python installation. At the terminal, type
   the following command:

        $ python3 -m venv ./venv

2. Activate the virtual environment:

        $ source ./venv/bin/activate

3. Install Python dependencies for this project:

        $ pip install -r requirements.txt

4. (Optional) Enable Django's debug mode for development:

        $ export DJANGO_DEBUG=True

5. Start the Django development server:

        $ python manage.py runserver

6. Open http://127.0.0.1:8000/ in a web browser to view your application.

What Do I Do Next?
------------------

Once you have a virtual environment running, you can start making changes to
the sample Django web application. We suggest making a small change to
/helloworld/templates/index.html first, so you can see how changes pushed to
your project's repository are automatically picked up and deployed to the Amazon EC2
instance by AWS Elastic Beanstalk. (You can watch the progress on your project dashboard.)
Once you've seen how that works, start developing your own code, and have fun!

To run your tests locally, go to the root directory of the sample code and run
the `python manage.py test` command, which AWS CodeBuild also runs through
your `buildspec.yml` file.

To test your new code during the release process, modify the existing tests or
add tests to the tests directory. AWS CodeBuild will run the tests during the
build stage of your project pipeline. You can find the test results
in the AWS CodeBuild console.

Learn more about AWS CodeBuild and how it builds and tests your application here:
https://docs.aws.amazon.com/codebuild/latest/userguide/concepts.html

Learn more about AWS CodeStar by reading the user guide.  Ask questions or make
suggestions on our forum.

User Guide: https://docs.aws.amazon.com/codestar/latest/userguide/welcome.html
Forum: https://forums.aws.amazon.com/forum.jspa?forumID=248

How Do I Add Template Resources to My Project?
------------------

To add AWS resources to your project, you'll need to edit the `template.yml`
file in your project's repository. You may also need to modify permissions for
your project's worker roles. After you push the template change, AWS CodeStar
and AWS CloudFormation provision the resources for you.

See the AWS CodeStar user guide for instructions to modify your template:
https://docs.aws.amazon.com/codestar/latest/userguide/how-to-change-project.html#customize-project-template

What Should I Do Before Running My Project in Production?
------------------

AWS recommends you review the security best practices recommended by the framework
author of your selected sample application before running it in production. You
should also regularly review and apply any available patches or associated security
advisories for dependencies used within your application.

Best Practices: https://docs.aws.amazon.com/codestar/latest/userguide/best-practices.html?icmpid=docs_acs_rm_sec
