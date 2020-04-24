package arduino.workshop.myapplication

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

class EmergencyCall: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.main_screen)

        val number = "+972526586120"
        val finalNumber = number.trim()
        val intent = Intent(Intent.ACTION_DIAL, Uri.parse("tel:" + Uri.encode(finalNumber)))
        startActivity(intent)
    }
}