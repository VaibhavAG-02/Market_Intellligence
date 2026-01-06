# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-01-06

### 🎉 Initial Release

#### Added
- **Dashboard Page**: Real-time multi-stock comparison with normalized performance charts
- **Technical Analysis Page**: RSI, MACD, Bollinger Bands, Moving Averages with pattern detection
- **Strategy Tester Page**: Backtest MA and RSI strategies against Buy & Hold benchmark
- **Multi-Stock Analyzer Page**: NEW feature for comparing multiple stocks simultaneously
- **Risk Simulator Page**: Monte Carlo simulation with VaR calculation
- **Dark Theme UI**: Crystal-clear, professional dark theme with perfect text visibility
- **Multi-Source Data**: Integration with Alpha Vantage, Twelve Data, and Yahoo Finance APIs
- **Comprehensive Legal Disclaimers**: Header banner and footer disclaimers

### Features Detail

#### Multi-Stock Analyzer
- Analyze up to 5 stocks at once
- Three ranking methods: Best Overall Return, Best Strategy Performance, Risk-Adjusted (Sharpe Ratio)
- Dynamic ranking (no re-analysis needed when switching)
- Performance comparison chart (normalized to base 100)
- Smart recommendations: Strong Buy, Buy, Hold, Avoid
- Stock selection with checkboxes
- Investment calculator with two allocation methods (Equal Split, Weighted by Performance)
- Portfolio summary with expected returns
- Complete risk metrics (Volatility, Sharpe Ratio)

#### Technical Indicators
- RSI (Relative Strength Index)
- MACD (Moving Average Convergence Divergence)
- Bollinger Bands
- Moving Averages (20, 50, 200-day)

#### Pattern Detection
- Golden Cross (MA50 crosses above MA200)
- Death Cross (MA50 crosses below MA200)
- RSI Overbought/Oversold
- Bollinger Band Breakouts

#### Risk Management
- Monte Carlo simulation (100-5000 paths)
- Value at Risk (VaR) calculation at 95% confidence
- Volatility analysis
- Sharpe Ratio calculation

### 🎨 Design
- Professional dark theme (#0f1419 background)
- Crystal-clear text (#ffffff)
- Purple-pink gradient accents (#6366f1 → #8b5cf6)
- Color-coded recommendations (green, yellow, orange, red)
- Interactive Plotly charts
- Responsive layout

### 📚 Documentation
- README.md with prominent disclaimers
- LEGAL_DISCLAIMER.md with comprehensive terms
- INSTALLATION.md with step-by-step setup
- CONTRIBUTING.md for open source guidelines
- CHANGELOG.md (this file)

### 🛡️ Legal Protection
- Prominent disclaimer banner at top
- Comprehensive footer disclaimer
- Clear "educational purposes only" messaging
- "Not financial advice" warnings throughout
- Limitation of liability clauses

### 🔧 Technical
- Python 3.8+ compatible
- Streamlit framework
- Session state management for persistent data
- Multi-API fallback system
- Error handling and rate limit management
- Caching for performance

---

## [Unreleased]

### Planned Features
- [ ] Options analysis module
- [ ] Portfolio tracking across sessions
- [ ] More technical indicators (Ichimoku, Fibonacci, etc.)
- [ ] Export reports to PDF
- [ ] Sector analysis
- [ ] Real-time alerts
- [ ] Historical comparison charts
- [ ] More allocation strategies
- [ ] Fundamental analysis integration
- [ ] News sentiment analysis

### Known Issues
- Free API tiers have rate limits (5 calls/min for Alpha Vantage)
- Yahoo Finance data can be unreliable
- Data delays of 5-20 minutes on free tiers
- Limited to daily data (no intraday)

### Future Improvements
- Add more data providers
- Implement user accounts (optional)
- Add export functionality
- Improve mobile responsiveness
- Add dark/light theme toggle
- Add more chart types
- Implement custom indicator builder

---

## Version History

### [1.0.0] - 2026-01-06
- Initial public release
- Core features implemented
- Legal disclaimers added
- Documentation completed

---

## How to Read This Changelog

- **Added**: New features
- **Changed**: Changes to existing functionality
- **Deprecated**: Features to be removed in future
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security updates

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on suggesting features or reporting bugs.

---

**Note**: This is an educational project. All features are for learning purposes only and do not constitute financial advice.
