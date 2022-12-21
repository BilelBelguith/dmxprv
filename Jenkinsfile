node {
    def SONARQUBE_HOSTNAME = 'https://sonar.fogits.com'
    stage('cloninig'){
     url: 'https://github.com/BilelBelguith/dmxprv.git'
      
      
    
    }
    stage ('config tools coverage'){
            sh "coverage run files_in_folder.py"
             sh "coverage xml"
     
        
    }

    stage('sonar analysis'){
        def scannerHome = tool 'sonarqube';
        withSonarQubeEnv('sonarqube'){
            sh "${scannerHome}/bin/sonar-scanner \
            -D sonar.login=bilel.belguith   \
            -D sonar.password=DMXfogits99 \
            -D sonar.projectKey=jenkinstest12 \
            -D sonar.python.version=3.0 \
            -D sonar.python.coverage.reportPaths=coverage.xml \
            -D sonar.host.url=https://sonar.fogits.com"
                }
    }

}
