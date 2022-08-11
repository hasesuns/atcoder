use proconio::input;

fn dfs(a: usize, b: usize, c: usize, memo: &mut Vec<Vec<Vec<Option<f64>>>>) -> f64 {
    if memo[a][b][c].is_some() {
        return memo[a][b][c].unwrap();
    }
    if a == 100 || b == 100 || c == 100 {
        return 0.;
    }
    let mut tmp = 0.;
    tmp += (dfs(a + 1, b, c, memo) + 1.) * a as f64 / (a + b + c) as f64;
    tmp += (dfs(a, b + 1, c, memo) + 1.) * b as f64 / (a + b + c) as f64;
    tmp += (dfs(a, b, c + 1, memo) + 1.) * c as f64 / (a + b + c) as f64;
    memo[a][b][c] = Some(tmp);
    return tmp;
}

fn main() {
    input! {
        (a, b, c): (usize, usize, usize)
    }
    let mut dp = vec![vec![vec![None; 101]; 101]; 101];
    let ans = dfs(a, b, c, &mut dp);
    println!("{}", ans);
}