package arduino.workshop.myapplication

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_register.*

class Register: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_register)

        registerButton.setOnClickListener {
            val userEmail = registeredEmail.text.toString()
            val userPhone = registeredPhoneNumber.text.toString()
            val braceletID = registeredBraceletId.text.toString()
            val password = registeredPassword.text.toString()

            var user = User(userEmail, userPhone, braceletID, password) // TODO: decide whether upload information to database or save locally
        }
    }
}