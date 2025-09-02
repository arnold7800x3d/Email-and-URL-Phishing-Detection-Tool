import { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { Label } from "@/components/ui/label";
import { Badge } from "@/components/ui/badge";
import { Shield, Mail, Link as LinkIcon, LogOut, AlertTriangle, CheckCircle } from "lucide-react";
import { useNavigate } from "react-router-dom";
import { useToast } from "@/hooks/use-toast";

interface AnalysisResult {
  prediction: "Phishing" | "Safe";
  probability: number;
  type: "email" | "url";
}

const Dashboard = () => {
  const [emailContent, setEmailContent] = useState("");
  const [urlFeatures, setUrlFeatures] = useState("");
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [results, setResults] = useState<AnalysisResult[]>([]);
  const navigate = useNavigate();
  const { toast } = useToast();

  useEffect(() => {
    // Check if user is logged in
    const isLoggedIn = localStorage.getItem("isLoggedIn");
    if (!isLoggedIn) {
      navigate("/login");
    }
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem("isLoggedIn");
    localStorage.removeItem("userEmail");
    toast({
      title: "Logged out",
      description: "You have been successfully logged out",
    });
    navigate("/");
  };

  const analyzeEmail = async () => {
    if (!emailContent.trim()) {
      toast({
        title: "Validation Error",
        description: "Please enter email content to analyze",
        variant: "destructive"
      });
      return;
    }

    setIsAnalyzing(true);
    
    try {
      // TODO: Replace with actual API call to /predict/email
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      // Mock result for demo
      const mockResult: AnalysisResult = {
        prediction: Math.random() > 0.5 ? "Safe" : "Phishing",
        probability: Math.random(),
        type: "email"
      };
      
      setResults(prev => [mockResult, ...prev]);
      
      toast({
        title: "Analysis Complete",
        description: `Email analyzed as ${mockResult.prediction}`,
      });
    } catch (error) {
      toast({
        title: "Analysis Failed",
        description: "Failed to analyze email. Please try again.",
        variant: "destructive"
      });
    } finally {
      setIsAnalyzing(false);
    }
  };

  const analyzeUrl = async () => {
    if (!urlFeatures.trim()) {
      toast({
        title: "Validation Error",
        description: "Please enter URL features to analyze",
        variant: "destructive"
      });
      return;
    }

    setIsAnalyzing(true);
    
    try {
      // TODO: Replace with actual API call to /predict/url
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      // Mock result for demo
      const mockResult: AnalysisResult = {
        prediction: Math.random() > 0.5 ? "Safe" : "Phishing",
        probability: Math.random(),
        type: "url"
      };
      
      setResults(prev => [mockResult, ...prev]);
      
      toast({
        title: "Analysis Complete",
        description: `URL analyzed as ${mockResult.prediction}`,
      });
    } catch (error) {
      toast({
        title: "Analysis Failed",
        description: "Failed to analyze URL. Please try again.",
        variant: "destructive"
      });
    } finally {
      setIsAnalyzing(false);
    }
  };

  const userEmail = localStorage.getItem("userEmail") || "user@example.com";

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center space-x-2">
            <Shield className="h-8 w-8 text-primary" />
            <h1 className="text-2xl font-bold">PhishGuard</h1>
          </div>
          <div className="flex items-center space-x-4">
            <span className="text-sm text-muted-foreground">{userEmail}</span>
            <Button variant="ghost" onClick={handleLogout}>
              <LogOut className="h-4 w-4 mr-2" />
              Logout
            </Button>
          </div>
        </div>
      </header>

      <div className="container mx-auto px-4 py-8">
        <div className="mb-8">
          <h2 className="text-3xl font-bold mb-2">Detection Dashboard</h2>
          <p className="text-muted-foreground">Analyze emails and URLs for potential phishing threats</p>
        </div>

        <div className="grid lg:grid-cols-2 gap-8">
          {/* Email Analysis */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center space-x-2">
                <Mail className="h-5 w-5" />
                <span>Email Analysis</span>
              </CardTitle>
              <CardDescription>
                Paste the suspicious email content below for analysis
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <div>
                <Label htmlFor="email-content">Email Content</Label>
                <Textarea
                  id="email-content"
                  placeholder="Paste the full email content here..."
                  value={emailContent}
                  onChange={(e) => setEmailContent(e.target.value)}
                  className="min-h-32 mt-2"
                />
              </div>
              <Button 
                onClick={analyzeEmail} 
                disabled={isAnalyzing}
                className="w-full"
              >
                {isAnalyzing ? "Analyzing..." : "Submit Email"}
              </Button>
            </CardContent>
          </Card>

          {/* URL Analysis */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center space-x-2">
                <LinkIcon className="h-5 w-5" />
                <span>URL Analysis</span>
              </CardTitle>
              <CardDescription>
                Enter URL numeric features for phishing detection
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <div>
                <Label htmlFor="url-features">URL Features</Label>
                <Textarea
                  id="url-features"
                  placeholder="Enter comma-separated numeric features (e.g., 1.2, 0.8, 2.1, ...)"
                  value={urlFeatures}
                  onChange={(e) => setUrlFeatures(e.target.value)}
                  className="min-h-32 mt-2"
                />
                <p className="text-sm text-muted-foreground mt-1">
                  Enter the extracted numeric features from the URL for analysis
                </p>
              </div>
              <Button 
                onClick={analyzeUrl} 
                disabled={isAnalyzing}
                className="w-full"
              >
                {isAnalyzing ? "Analyzing..." : "Submit URL"}
              </Button>
            </CardContent>
          </Card>
        </div>

        {/* Results Section */}
        {results.length > 0 && (
          <Card className="mt-8">
            <CardHeader>
              <CardTitle>Analysis Results</CardTitle>
              <CardDescription>
                Recent phishing detection results
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {results.map((result, index) => (
                  <div key={index} className="flex items-center justify-between p-4 border rounded-lg">
                    <div className="flex items-center space-x-4">
                      {result.type === "email" ? (
                        <Mail className="h-5 w-5 text-muted-foreground" />
                      ) : (
                        <LinkIcon className="h-5 w-5 text-muted-foreground" />
                      )}
                      <div>
                        <p className="font-medium capitalize">{result.type} Analysis</p>
                        <p className="text-sm text-muted-foreground">
                          Confidence: {(result.probability * 100).toFixed(1)}%
                        </p>
                      </div>
                    </div>
                    <div className="flex items-center space-x-2">
                      {result.prediction === "Phishing" ? (
                        <>
                          <AlertTriangle className="h-4 w-4 text-destructive" />
                          <Badge variant="destructive">Phishing</Badge>
                        </>
                      ) : (
                        <>
                          <CheckCircle className="h-4 w-4 text-green-600" />
                          <Badge className="bg-green-100 text-green-800 hover:bg-green-100">Safe</Badge>
                        </>
                      )}
                    </div>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        )}
      </div>
    </div>
  );
};

export default Dashboard;