package arduino.workshop.myapplication

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_sign_in.*
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

class MainActivity : AppCompatActivity() {

    @ExperimentalStdlibApi
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_sign_in)

        var usernameFromApp = ""
        var passwordFromDataBase = ""
        var userNameFromDataBase = ""
        var valuesFromDataBase = ""
        var nameAndArdId = ""

        registerButton.setOnClickListener {
            startActivity(Intent(this, Register::class.java))
        }

        signInButton.setOnClickListener {
            usernameFromApp = signInEmail.text.toString()
            val passwordFromApp = signInPassword.text.toString()
            CoroutineScope(Dispatchers.IO).launch {
                nameAndArdId = ClientSocket.doInBackground(
                    "signin;".plus(usernameFromApp).plus(";").plus(passwordFromApp)).toString()
            }

            if (nameAndArdId != ("-1")) {
                valuesFromDataBase = nameAndArdId.split(";").toString()
                var newUser =
                    User(
                        valuesFromDataBase?.get(0).toString(),
                        usernameFromApp,
                        valuesFromDataBase?.get(1).toString()
                    )
                startActivity(Intent(this, ScreenMain::class.java))
            }
            else {
                Toast.makeText(this@MainActivity, "User Could Not Be Found!", Toast.LENGTH_SHORT)
                    .show()
            }
        }


    }
}
