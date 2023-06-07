```
amplify init
```

Then all defaults

```
amplify add auth

Using service: Cognito, provided by: awscloudformation

 The current configured provider is Amazon Cognito.

 Do you want to use the default authentication and security configuration? Manual configuration
 Select the authentication/authorization services that you want to use: User Sign-Up, Sign-In, connected with AWS IAM controls (Enables per-user Storage features for images or other content, Analytics, and mor
e)
 Provide a friendly name for your resource that will be used to label this category in the project: frontend829bd435829bd435
 Enter a name for your identity pool. frontend829bd435_identitypool_829bd435
 Allow unauthenticated logins? (Provides scoped down permissions that you can control via AWS IAM) Yes
 Do you want to enable 3rd party authentication providers in your identity pool? Yes
 Select the third party identity providers you want to configure for your identity pool:
 Provide a name for your user pool: frontend829bd435_userpool_829bd435
 How do you want users to be able to sign in? Username
 Do you want to add User Pool Groups? No
 Do you want to add an admin queries API? No
 Multifactor authentication (MFA) user login options: OFF
 Email based user registration/forgot password: Enabled (Requires per-user email entry at registration)
 Specify an email verification subject: Your verification code
 Specify an email verification message: Your verification code is {####}
 Do you want to override the default password policy for this User Pool? No
 Warning: you will not be able to edit these selections.
 What attributes are required for signing up? Email
 Specify the app's refresh token expiration period (in days): 30
 Do you want to specify the user attributes this app can read and write? No
 Do you want to enable any of the following capabilities?
 Do you want to use an OAuth flow? Yes
 What domain name prefix do you want to use? frontend829bd435-829bd435
 Enter your redirect signin URI:
PS C:\Users\damie\Projets GIT\CLD_Workshop_23\face_liveness\frontend> amplify add auth
Using service: Cognito, provided by: awscloudformation

 The current configured provider is Amazon Cognito.

 Do you want to use the default authentication and security configuration? Manual configuration
 Select the authentication/authorization services that you want to use: User Sign-Up, Sign-In, connected with AWS IAM controls (Enables per-user Storage features for images or other content, Analytics, and mor
e)
 Provide a friendly name for your resource that will be used to label this category in the project: frontend66c6f59666c6f596
 Enter a name for your identity pool. frontend66c6f596_identitypool_66c6f596
 Allow unauthenticated logins? (Provides scoped down permissions that you can control via AWS IAM) Yes
 Do you want to enable 3rd party authentication providers in your identity pool? No
 Provide a name for your user pool: frontend66c6f596_userpool_66c6f596
 Warning: you will not be able to edit these selections.
 How do you want users to be able to sign in? Username
 Do you want to add User Pool Groups? No
 Do you want to add an admin queries API? No
 Multifactor authentication (MFA) user login options: OFF
 Email based user registration/forgot password: Disabled (Uses SMS/TOTP as an alternative)
 Please specify an SMS verification message: Your verification code is {####}
 Do you want to override the default password policy for this User Pool? No
 Warning: you will not be able to edit these selections.
 What attributes are required for signing up? Email
 Specify the app's refresh token expiration period (in days): 30
 Do you want to specify the user attributes this app can read and write? No
 Do you want to enable any of the following capabilities?
 Do you want to use an OAuth flow? No
? Do you want to configure Lambda Triggers for Cognito? No
✅ Successfully added auth resource frontend66c6f59666c6f596 locally

✅ Some next steps:
"amplify push" will build all your local backend resources and provision it in the cloud
"amplify publish" will build all your local backend and frontend resources (if you have hosting category added) and provision it in the cloud
```

```
amplify push
```