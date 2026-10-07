package com.miui.securitycenter;

import android.app.Activity;
import android.os.Bundle;

/**
 * Stub replacing MIUI's Security Center for the camera's CTA agreement:
 * answers the permission-declare intents with result code 1.
 */
public class CtaActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setResult(1);
        finish();
    }
}
