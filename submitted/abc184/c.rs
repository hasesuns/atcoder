use proconio::input;

fn main() {
    input! {
        (r1, c1): (i64, i64),
        (r2, c2): (i64, i64)
    }
    if r1 == r2 && c1 == c2 {
        println!("0");
        return;
    }
    if r1 + c1 == r2 + c2 || r1 - c1 == r2 - c2 || (r1 - r2).abs() + (c1 - c2).abs() <= 3 {
        println!("1");
        return;
    }
    if (r1 + c1) % 2 == (r2 + c2) % 2 {
        println!("2");
        return;
    }
    for dy in -3i64..=3i64 {
        let ddx = 3 - dy.abs();
        for dx in -ddx..=ddx {
            let ny = r2 + dy;
            let nx = c2 + dx;
            if r1 + c1 == nx + ny || r1 - c1 == ny - nx {
                println!("2");
                return;
            }
        }
    }
    if (r1 - r2).abs() + (c1 - c2).abs() <= 6 {
        println!("2");
        return;
    }
    println!("3");
}