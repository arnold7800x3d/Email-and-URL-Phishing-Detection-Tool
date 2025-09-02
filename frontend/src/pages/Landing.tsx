import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Shield, Lock, Eye, CheckCircle } from "lucide-react";
import { Link } from "react-router-dom";

const Landing = () => {
  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center space-x-2">
            <Shield className="h-8 w-8 text-primary" />
            <h1 className="text-2xl font-bold">PhishGuard</h1>
          </div>
          <div className="space-x-4">
            <Button variant="ghost" asChild>
              <Link to="/login">Login</Link>
            </Button>
            <Button asChild>
              <Link to="/signup">Get Started</Link>
            </Button>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="py-20 px-4">
        <div className="container mx-auto text-center max-w-4xl">
          <h2 className="text-4xl md:text-6xl font-bold mb-6">
            Protect Yourself from <span className="text-primary">Phishing Attacks</span>
          </h2>
          <p className="text-xl text-muted-foreground mb-8 max-w-2xl mx-auto">
            Advanced AI-powered detection to identify malicious emails and URLs before they compromise your security.
          </p>
          <Button size="lg" className="text-lg px-8 py-6" asChild>
            <Link to="/signup">Start Free Detection</Link>
          </Button>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 px-4 bg-muted/50">
        <div className="container mx-auto max-w-6xl">
          <h3 className="text-3xl font-bold text-center mb-12">Key Features</h3>
          <div className="grid md:grid-cols-3 gap-8">
            <Card>
              <CardHeader>
                <Lock className="h-12 w-12 text-primary mb-4" />
                <CardTitle>Email Analysis</CardTitle>
                <CardDescription>
                  Analyze email content using advanced machine learning algorithms to detect phishing attempts.
                </CardDescription>
              </CardHeader>
            </Card>
            <Card>
              <CardHeader>
                <Eye className="h-12 w-12 text-primary mb-4" />
                <CardTitle>URL Scanning</CardTitle>
                <CardDescription>
                  Check suspicious URLs and websites for malicious content and phishing indicators.
                </CardDescription>
              </CardHeader>
            </Card>
            <Card>
              <CardHeader>
                <CheckCircle className="h-12 w-12 text-primary mb-4" />
                <CardTitle>Real-time Results</CardTitle>
                <CardDescription>
                  Get instant probability scores and detailed analysis to make informed decisions.
                </CardDescription>
              </CardHeader>
            </Card>
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="py-20 px-4">
        <div className="container mx-auto max-w-4xl">
          <h3 className="text-3xl font-bold text-center mb-12">How It Works</h3>
          <div className="grid md:grid-cols-2 gap-8 items-center">
            <div>
              <div className="space-y-6">
                <div className="flex items-start space-x-4">
                  <div className="bg-primary text-primary-foreground rounded-full w-8 h-8 flex items-center justify-center font-bold">1</div>
                  <div>
                    <h4 className="font-semibold mb-2">Upload Content</h4>
                    <p className="text-muted-foreground">Paste suspicious email content or enter URL details for analysis.</p>
                  </div>
                </div>
                <div className="flex items-start space-x-4">
                  <div className="bg-primary text-primary-foreground rounded-full w-8 h-8 flex items-center justify-center font-bold">2</div>
                  <div>
                    <h4 className="font-semibold mb-2">AI Analysis</h4>
                    <p className="text-muted-foreground">Our advanced AI models process and analyze the content for threats.</p>
                  </div>
                </div>
                <div className="flex items-start space-x-4">
                  <div className="bg-primary text-primary-foreground rounded-full w-8 h-8 flex items-center justify-center font-bold">3</div>
                  <div>
                    <h4 className="font-semibold mb-2">Get Results</h4>
                    <p className="text-muted-foreground">Receive detailed results with probability scores and recommendations.</p>
                  </div>
                </div>
              </div>
            </div>
            <div className="bg-muted rounded-lg p-8 text-center">
              <Shield className="h-24 w-24 text-primary mx-auto mb-4" />
              <p className="text-lg font-semibold">Secure & Private</p>
              <p className="text-muted-foreground mt-2">Your data is processed securely and never stored permanently.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-muted py-12 px-4">
        <div className="container mx-auto text-center">
          <div className="flex items-center justify-center space-x-2 mb-4">
            <Shield className="h-6 w-6 text-primary" />
            <span className="text-lg font-semibold">PhishGuard</span>
          </div>
          <p className="text-muted-foreground">© 2024 PhishGuard. Protecting you from digital threats.</p>
        </div>
      </footer>
    </div>
  );
};

export default Landing;