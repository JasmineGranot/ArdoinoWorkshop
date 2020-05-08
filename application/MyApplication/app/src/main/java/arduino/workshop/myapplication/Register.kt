package arduino.workshop.myapplication

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_current_pulse.*
import kotlinx.android.synthetic.main.activity_register.*
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

class Register: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_register)

        registerButton.setOnClickListener {
            val userName = registeredName.text.toString()
            val userEmail = registeredEmail.text.toString()
            val userPhone = registeredPhoneNumber.text.toString()
            val braceletID = registeredBraceletId.text.toString()
            val password = registeredPassword.text.toString()

            if(userName.isEmpty()) {
                Toast.makeText(this@Register, "Must Insert User Name!", Toast.LENGTH_SHORT).show()
            }
            else if(userEmail.isEmpty()) {
                Toast.makeText(this@Register, "Must Insert User Email!", Toast.LENGTH_SHORT).show()
            }
            else if(userPhone.isEmpty()) {
                Toast.makeText(this@Register, "Must Insert User Phone!", Toast.LENGTH_SHORT).show()
            }
            else if(braceletID.isEmpty()) {
                Toast.makeText(this@Register, "Must Insert Bracelet ID!", Toast.LENGTH_SHORT).show()
            }
            else if(password.isEmpty()) {
                Toast.makeText(this@Register, "Must Insert Password!", Toast.LENGTH_SHORT).show()
            }
            else {

                val newUserName = userName.replace(' ', '-')
                var user = User(
                    userName,
                    userEmail,
                    userPhone,
                    braceletID,
                    password
                ) // TODO: decide whether upload information to database or save locally
                val userInfo =
                    newUserName.plus(" ").plus(userEmail).plus(" ").plus(userPhone).plus(" ")
                        .plus(braceletID).plus(" ").plus(password).plus("")
                CoroutineScope(Dispatchers.IO).launch {
                    ClientSocket.doInBackground(userInfo)
                }
            }
        }
    }
}