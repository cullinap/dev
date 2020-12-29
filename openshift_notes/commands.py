# Answers

# smoke test questions
question1a = "oc new-app --name hello-world-nginx --as-deployment-config https://github.com/RedHatTraining/DO280-apps --context-dir hello-world-nginx"
question1b = "Create a route to the application by exposing the hello-world-nginx service"
question1c = "oc expose service hello-world-nginx --hostname hello-world.apps.ocp4.example.com"
question1d = "Wait until the application pod is running"
question1e = "oc get pods"
question1f = "Verify access to the application"
question1g = "curl -s http://hello-world.apps.ocp4.example.com | grep Hello"

# identity providers question
question2a = "oc new-app --name hello-world-nginx --as-deployment-config https://github.com/RedHatTraining/DO280-apps --context-dir hello-world-nginx"
question2b = "Create a route to the application by exposing the hello-world-nginx service"
question2c = "oc expose service hello-world-nginx --hostname hello-world.apps.ocp4.example.com"
question2d = "Wait until the application pod is running"
question2e = "oc get pods"
question2f = "Verify access to the application"
question2g = "curl -s http://hello-world.apps.ocp4.example.com | grep Hello"