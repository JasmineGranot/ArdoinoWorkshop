package arduino.workshop.myapplication

import android.content.Intent
import android.os.Build
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_sign_in.*
import java.net.HttpURLConnection
import java.net.URL

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_sign_in)

        registerButton.setOnClickListener {
            startActivity(Intent(this, Register::class.java))
        }

        signInButton.setOnClickListener {
            val usernameFromApp = signInEmail.text.toString()
            val passwordFromApp = signInPassword.text.toString()
            val userNameFromDataBase = "veredh12@hotmail.com"
            val passwordFromDataBase = "123456"

            if (usernameFromApp == userNameFromDataBase && passwordFromApp == passwordFromDataBase) {
                startActivity(Intent(this, ScreenMain::class.java))
            } else if (usernameFromApp != userNameFromDataBase && passwordFromApp == passwordFromDataBase) {
                Toast.makeText(this@MainActivity, "Email Is Incorrect", Toast.LENGTH_SHORT).show()
            } else if (passwordFromApp != passwordFromDataBase && usernameFromApp == userNameFromDataBase) {
                Toast.makeText(this@MainActivity, "Password Is Incorrect", Toast.LENGTH_SHORT)
                    .show()
            } else {
                Toast.makeText(this@MainActivity, "User Is Not Registered", Toast.LENGTH_SHORT)
                    .show()
            }
        }
    }
}
