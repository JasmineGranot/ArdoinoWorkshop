package arduino.workshop.myapplication

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_sign_in.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_sign_in)

        registerButton.setOnClickListener {
            startActivity(Intent(this, Register::class.java))
        }

        signInButton.setOnClickListener {
            val username = signInEmail.text.toString()
            val password = signInPassword.text.toString()

            if(username == "veredh12@hotmail.com" && password == "123456") {
                startActivity(Intent(this, ScreenMain::class.java))
            }
        }
    }
}
