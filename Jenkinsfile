node {
    def SONARQUBE_HOSTNAME = 'https://sonar.fogits.com'
    stage('cloninig'){
    git branch :'staging',
      credentialsId: '4b3eeb60-a313-4d10-b4ef-a1eccee86686', 
      url: 'https://github.com/BilelBelguith/dmxprv.git'
    
    }
  

    stage('sonar-scanner') {
      def sonarqubeScannerHome = tool name: 'sonarqube', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
      withCredentials([string(credentialsId: 'DMXfogits99', variable: 'bilel.belguith')]) {
        sh "${sonarqubeScannerHome}/bin/sonar-scanner -e -Dsonar.host.url=http://${SONARQUBE_HOSTNAME} -Dsonar.login=bilel.belguith -Dsonar.projectKey=jenkinstest12 "
      }
    }

}
