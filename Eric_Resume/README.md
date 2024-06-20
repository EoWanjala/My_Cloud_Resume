# CLOUD MY TRIBE: MY CLOUD RESUME PROJECT
## Project Goal
Create your resume and deploy it to Cloud making use of Amazon S3, CloudFront and Route 53
## Architectural Diagram
The diagram was designed using Lucid Charts
![website to cloud](https://github.com/EoWanjala/My_Cloud_Resume/assets/111036656/d18c777d-b977-4fba-91e6-159a2fe6f120)

## Services
1. Amazon S3
  - Create a bucket and enable public access
  - Static Website hosting was enabled.
  - The bucket name was same as the dormain name purchased
  - The website documentation were uploaded to the bucket and the eric_resume.html file referenced
2. Route 53
  - Create a hosted zone
  - Gave the hosted zone the same name as my dormain purchased
  - Copied the ns-records brought and registered them with my dormain name provider(HostAfrica.co.ke)
  - Created an Alias Record to Amazon S3 and CloudFront
3. CloudFront
  - Created a distribution same to my S3 name
  - Created a Certificate , with a redirect to the Certificate Manager

## Video

## Challenges Encountered
I had a challenge with creating my cloudfront distribution, requiring my account be verified before creation. It took about 4 days.

## Future Improvement
Implement CI/CD Pipeline together with GitHub 

## Acknowledgements
Props to Ann Andega for the .html and .css file template
Light Situma for his guidance
CloudMyTribe

## Authors
Eric Wanjala

    
