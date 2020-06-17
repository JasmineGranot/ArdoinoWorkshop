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
        var nameAndArdId = "-1"

        registerButton.setOnClickListener {
            startActivity(Intent(this, Register::class.java))
        }

        signInButton.setOnClickListener {
            usernameFromApp = signInEmail.text.toString()
            val passwordFromApp = signInPassword.text.toString()
            CoroutineScope(Dispatchers.IO).launch {
                //val isSocketOpen = MySocket.doInBackground("")
                //if(isSocketOpen.equals("true")) {}
                nameAndArdId = ClientSocket.doInBackground(
                    "signin;".plus(usernameFromApp).plus(";").plus(passwordFromApp)
                ).toString()
            }.invokeOnCompletion {
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

    override fun finishActivity(requestCode: Int) {
        super.finishActivity(requestCode)
        MySocket.closeSocket()
    }
}
