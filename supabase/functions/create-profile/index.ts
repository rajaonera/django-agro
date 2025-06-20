import { serve } from 'https://deno.land/std/http/server.ts';

serve(async (req) => {
  if (req.method === 'OPTIONS') {
    return new Response("OK", {
      status: 200,
      headers: {
        "Access-Control-Allow-Origin": "http://localhost:8080",
        "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Authorization",
      },
    });
  }

  try {
    const { uid, email } = await req.json();

    // Appel de ta fonction RPC
    const supabaseUrl = Deno.env.get("SUPABASE_URL")!;
    const supabaseKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
      
    const client = supabase.createClient(supabaseUrl, supabaseKey);
    
    const { data, error } = await client.rpc("create_profile_if_not_exists", { uid, email });

    if (error) {
      return new Response(JSON.stringify({ error: error.message }), {
        status: 400,
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "http://localhost:8080"
        },
      });
    }

    return new Response(JSON.stringify({ message: "Profil créé ou confirmé.", data }), {
      status: 200,
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "http://localhost:8080"
      },
    });

  } catch (err) {
    return new Response(JSON.stringify({ error: err.message }), {
      status: 500,
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "http://localhost:8080"
      },
    });
  }
});
