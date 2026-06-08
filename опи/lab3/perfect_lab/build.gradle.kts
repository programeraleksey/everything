plugins {
    war
}

repositories {
    mavenCentral()
}

dependencies {
    compileOnly("javax:javaee-api:8.0.1")
    implementation("org.primefaces:primefaces:13.0.0")
    implementation("org.postgresql:postgresql:42.7.8")
}

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(17)
    }
}
